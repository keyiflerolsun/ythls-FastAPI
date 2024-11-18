# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI                 import konsol
from pymongo             import MongoClient, ASCENDING
from pymongo.collection  import Collection
from pymongo.database    import Database
from motor.motor_asyncio import AsyncIOMotorClient
from deepdiff            import DeepDiff
from bson.json_util      import dumps, loads
import os

class SineWixDB:
    def __init__(self, db_url="mongodb://keyif:kekik@10.0.1.0:27017", db_name="SineWixDB"):
        self.client:MongoClient = AsyncIOMotorClient(db_url)
        self.db:Database        = self.client[db_name]

        self.movies:Collection = self.db["movies"]
        self.series:Collection = self.db["series"]
        self.animes:Collection = self.db["animes"]

        self.movie_details:Collection  = self.db["movie_details"]
        self.series_details:Collection = self.db["series_details"]
        self.anime_details:Collection  = self.db["anime_details"]

        self.movies.create_index([("id", ASCENDING)], unique=True)
        self.series.create_index([("id", ASCENDING)], unique=True)
        self.animes.create_index([("id", ASCENDING)], unique=True)

        self.movie_details.create_index([("id", ASCENDING)], unique=True)
        self.series_details.create_index([("id", ASCENDING)], unique=True)
        self.anime_details.create_index([("id", ASCENDING)], unique=True)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    async def add_movie(self, data: dict) -> bool:
        return await self._add_item(self.movies, data)

    async def add_series(self, data: dict) -> bool:
        return await self._add_item(self.series, data)

    async def add_anime(self, data: dict) -> bool:
        return await self._add_item(self.animes, data)

    async def add_movie_detail(self, detail: dict) -> bool:
        return await self._add_item(self.movie_details, detail)

    async def add_series_detail(self, detail: dict) -> bool:
        return await self._add_item(self.series_details, detail)

    async def add_anime_detail(self, detail: dict) -> bool:
        return await self._add_item(self.anime_details, detail)

    async def get_movie_by_id(self, movie_id: int) -> dict:
        return await self._get_item_by_id(self.movies, movie_id)

    async def get_series_by_id(self, series_id: int) -> dict:
        return await self._get_item_by_id(self.series, series_id)

    async def get_anime_by_id(self, anime_id: int) -> dict:
        return await self._get_item_by_id(self.animes, anime_id)

    async def get_movie_details(self, movie_id: int) -> list[dict]:
        return await self._get_details(self.movie_details, movie_id)

    async def get_series_details(self, series_id: int) -> list[dict]:
        return await self._get_details(self.series_details, series_id)

    async def get_anime_details(self, anime_id: int) -> list[dict]:
        return await self._get_details(self.anime_details, anime_id)

    async def search(self, search_term: str) -> dict:
        search_results = {}

        search_results["movies"] = await self._search_collection(self.movie_details, search_term, ["title", "original_name"])
        search_results["series"] = await self._search_collection(self.series_details, search_term, ["name", "original_name"])
        search_results["animes"] = await self._search_collection(self.anime_details, search_term, ["name", "original_name"])

        return search_results

    async def _search_collection(self, collection, search_term: str, fields: list[str]) -> list[dict]:
        query   = {
            "$or" : [{field: {"$regex": search_term, "$options": "i"}} for field in fields]
        }
        veriler = await collection.find(query, {"_id": 0}).sort("id", -1).limit(12).to_list(None)

        if not veriler:
            return []

        return [
            {
                "id"          : veri["id"],
                "name"        : veri.get("name") or veri.get("title") or veri.get("original_name"),
                "poster_path" : veri["poster_path"],
                "type"        : collection.name.split("_")[0].replace("series", "serie")
            }
                for veri in veriler
        ]

    async def _add_item(self, collection, data: dict, exclude_keys=None) -> bool:
        if exclude_keys is None:
            exclude_keys = ["views", "time", "updated_at", "comments", "vote_average"]

        existing_item = await collection.find_one({"id": data.get("id")}, {"_id": 0})

        if existing_item:
            fark_var = await self._compare_and_clean_data(existing_item, data, exclude_keys)
            if fark_var:
                await collection.replace_one({"id": data.get("id")}, data)
                return True

            return False

        await collection.insert_one(data)
        return True

    async def _compare_and_clean_data(self, existing_data: dict, new_data: dict, exclude_keys: list[str]) -> bool:
        """
        Mevcut veri ve yeni veri arasındaki farkları karşılaştırır ve belirtilen anahtarları hariç tutar.
        Eğer fark varsa True döner, yoksa False.
        """
        def clean_data(data:dict|list, keys_to_exclude: list[str]):
            """
            Veriyi temizler ve belirtilen anahtarları hariç tutar.
            Hem dict hem de list veri türlerini işleyebilir.
            """
            if isinstance(data, dict):
                return {key: clean_data(value, keys_to_exclude) for key, value in data.items() if key not in keys_to_exclude}

            if isinstance(data, list):
                return [clean_data(item, keys_to_exclude) for item in data]

        cleaned_existing_data = clean_data(existing_data, exclude_keys)
        cleaned_new_data      = clean_data(new_data, exclude_keys)

        differences = DeepDiff(cleaned_existing_data, cleaned_new_data, ignore_order=True)
        if differences:
            konsol.log(f"[bold red]Fark bulundu:[/] {differences}")

        return bool(differences)

    async def _get_item_by_id(self, collection, item_id: int) -> dict:
        return await collection.find_one({"id": item_id}, {"_id": 0})

    async def _get_details(self, collection, item_id: int) -> list[dict]:
        return await collection.find_one({"id": item_id}, {"_id": 0})

    async def get_movie_page(self, page: int, per_page: int = 12, genre_id: int = None) -> list[dict]:
        return await self._get_page(self.movies, page, per_page, genre_id)

    async def get_series_page(self, page: int, per_page: int = 12, genre_id: int = None) -> list[dict]:
        return await self._get_page(self.series, page, per_page, genre_id)

    async def get_anime_page(self, page: int, per_page: int = 12, genre_id: int = None) -> list[dict]:
        return await self._get_page(self.animes, page, per_page, genre_id)

    async def _get_page(self, collection, page: int, per_page: int, genre_id: int = None) -> list[dict]:
        skip = (page - 1) * per_page

        if not genre_id:
            return await collection.find({}, {"_id": 0}).sort("id", -1).skip(skip).limit(per_page).to_list(per_page)
        else:
            return await collection.find({"genres.genre_id": genre_id}, {"_id": 0}).sort("id", -1).skip(skip).limit(per_page).to_list(per_page)

    async def export_to_json(self):
        output_dir = f"./{self.db.name}"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        collections = await self.db.list_collection_names()
        for collection_name in collections:
            collection:Collection = self.db[collection_name]
            documents             = await collection.find({}).to_list(None)

            json_data = dumps(documents, indent=2, ensure_ascii=False, sort_keys=False)
            
            with open(f"{output_dir}/{collection_name}.json", "w", encoding="utf-8") as json_file:
                json_file.write(json_data)

            konsol.log(f"[green][+] Exported » {self.db.name} » {collection_name}")

    async def import_from_json(self):
        input_dir = f"./{self.db.name}"

        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"The directory {input_dir} does not exist.")

        for file_name in os.listdir(input_dir):
            if file_name.endswith(".json"):
                collection_name       = file_name.split(".json")[0]
                collection:Collection = self.db[collection_name]

                with open(os.path.join(input_dir, file_name), "r", encoding="utf-8") as json_file:
                    data      = json_file.read()
                    documents = loads(data)

                if isinstance(documents, list):
                    await collection.insert_many(documents)
                else:
                    await collection.insert_one(documents)

                konsol.log(f"[green][+] Imported » {self.db.name} » {file_name}")