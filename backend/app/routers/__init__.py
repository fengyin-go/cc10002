"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import metricdef as router_metricdef
from app.routers import dimension as router_dimension
from app.routers import datasource as router_datasource
from app.routers import aggregation as router_aggregation
from app.routers import dashboard as router_dashboard
from app.routers import cohort as router_cohort
from app.routers import abtest as router_abtest
from app.routers import report as router_report
from app.routers import alert as router_alert
from app.routers import datamine as router_datamine
from app.routers import api as router_api
from app.routers import etljob as router_etljob
from app.routers import quality as router_quality
from app.routers import datamodel as router_datamodel
from app.routers import export as router_export
from app.routers import subscribe as router_subscribe
from app.routers import lineage as router_lineage
from app.routers import segment as router_segment

ROUTERS = [router_metricdef, router_dimension, router_datasource, router_aggregation, router_dashboard, router_cohort, router_abtest, router_report, router_alert, router_datamine, router_api, router_etljob, router_quality, router_datamodel, router_export, router_subscribe, router_lineage, router_segment]
