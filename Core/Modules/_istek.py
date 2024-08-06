# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI                  import konsol
from Core                 import kekik_FastAPI, Request
from time                 import time
from user_agents          import parse
from Core.Modules._IP_Log import ip_log

@kekik_FastAPI.middleware("http")
async def istekten_once_sonra(request: Request, call_next):
    baslangic_zamani = time()

    if request.method == "GET":
        request.state.req_veri = dict(request.query_params) if request.query_params else None
    else:
        try:
            request.state.req_veri = await request.json()
        except Exception:
            form_data = await request.form()
            request.state.req_veri = dict(form_data.items())

    response   = await call_next(request)
    gecen_sure = time() - baslangic_zamani

    for path in ("/favicon.ico", "/static", "/webfonts"):
        if path in request.url.path:
            return response

    try:
        if str(parse(request.headers.get("User-Agent"))).split("/")[2].strip() == "Other":
            cihaz = request.headers.get("User-Agent")
        else:
            cihaz = parse(request.headers.get("User-Agent"))
    except TypeError:
        cihaz = request.headers.get("User-Agent")

    log_ip   = request.headers.get("X-Forwarded-For") or request.client.host
    ip_w_cf  = f"{request.headers.get('Cf-Connecting-Ip')} [yellow]| CF: ({log_ip})[/]" if request.headers.get("Cf-Connecting-Ip") else log_ip

    log_veri = {
        "id"     : request.headers.get("X-Request-ID") or "",
        "method" : request.method,
        "url"    : str(request.url).rstrip("?").split("?")[0],
        "veri"   : request.state.req_veri,
        "kod"    : response.status_code,
        "sure"   : round(gecen_sure, 2),
        "ip"     : log_ip,
        "cihaz"  : cihaz,
        "host"   : request.url.hostname,
    }

    log_url = log_veri['url'].replace(request.url.scheme, request.headers.get("X-Forwarded-Proto")) if request.headers.get("X-Forwarded-Proto") else log_veri['url']

    endpoint_bilgisi = f"[bold blue]»[/] [bold turquoise2]{log_url}[/]"
    data_bilgisi     = f"[blue]|[/] [green]veri:[/] [bold turquoise2]{log_veri['veri']}[/]" if log_veri["veri"] else ""

    konsol.log(f"{endpoint_bilgisi} {data_bilgisi}")
    konsol.log(f"[bold bright_blue]{log_veri['id']}[/][bold green]@[/][bold red]{log_veri['ip']}[/]\t[blue]|[/] [green]cihaz:[/] [magenta]{log_veri['cihaz']}[/] [blue]|[/] [bold green]{log_veri['method']}[/] [blue]-[/] [bold bright_yellow]{log_veri['kod']}[/] [blue]-[/] [bold yellow2]{log_veri['sure']}sn[/]")

    ip_detay = await ip_log(log_veri["ip"].split()[0])
    if ("hata" not in list(ip_detay.keys())) and (ip_detay["ulke"]):
        konsol.log(f"[bold chartreuse3]{ip_detay['ulke']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['il']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['sirket']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['isp']}[/] [blue]|[/] [bold chartreuse3]{ip_detay['host']}[/]")

    return response