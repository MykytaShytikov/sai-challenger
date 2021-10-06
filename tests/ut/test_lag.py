import pytest
from sai import SaiObject


@pytest.fixture(scope="module")
def sai_lag_obj(npu):
    lag_oid = npu.create(SaiObject.LAG, [])
    yield lag_oid
    npu.remove(lag_oid)


@pytest.fixture(scope="module")
def sai_lag_member(npu, sai_lag_obj):
    npu.remove_lag_member(npu.default_lag_obj)
    lag_mbr_oid = npu.careate_lag_member(sai_lag_obj)
    npu.set(npu.port_oids[0], "SAI_PORT_ATTR_LAG")
    yield lag_mbr_oid, sai_lag_obj
    npu.remove(lag_mbr_oid)
    npu.create_lag_member(npu.default_lag_obj)
    npu.set(npu.port_oid[0], "SAI_PORT_ATTR_LAG")


lag_attrs = [
    ("SAI_LAG_ATTR_PORT_LIST",                  "sai_object_list_t",    "0:null"),
    ("SAI_LAG_ATTR_INGRESS_ACL",                "sai_object_id_t",      "SAI_NULL_OBJECT_ID"),
    ("SAI_LAG_ATTR_EGRESS_ACL",                 "sai_object_id_t",      "SAI_NULL_OBJECT_ID"),
    ("SAI_LAG_ATTR_PORT_VLAN_ID",               "sai_uint16_t",         "1"),
    ("SAI_LAG_ATTR_DEFAULT_VLAN_PRIORITY",      "sai_uint8_t",          "0"),
    ("SAI_LAG_ATTR_DROP_UNTAGGED",              "bool",                 "false"),
    ("SAI_LAG_ATTR_DROP_TAGGED",                "bool",                 "false"),
    ("SAI_LAG_ATTR_TPID",                       "sai_uint16_t",         "0x8100"),
    ("SAI_LAG_ATTR_SYSTEM_PORT_AGGREGATE_ID",   "sai_uint32_t",         "0"),
    ("SAI_LAG_ATTR_LABEL",                      "char",                 ""),
]
