# 전체 페이지 목록 집계
from . import main, areas_hub, areas, stations, themes, info, magazine, about

PAGES = (
    [main.PAGE, areas_hub.HUB]
    + areas.PAGES
    + stations.PAGES
    + themes.PAGES
    + info.PAGES
    + magazine.PAGES
    + [about.PAGE]
)
