from enum import Enum

class MixinRules(Enum):
    LANG_AND_DEPTH_PERCEPTION = "rm001"
    ISHIHARA_AND_PERCEPTION_OF_COLOR = "rm002"

rules_ophthalmological_mixin_test = [
    {
        "id": 1,
        "code_rule": "rm001",
        "clasic_test_min_porcentaje": 57,
        "virtual_task_min_porcentaje": 40,
        "msg_in_range" : "Se ha encontrado una posible deficiencia visual de estereopsis",
        "msg_out_range" : "No se ha encontrado una posible deficiencia visual de estereopsis"
    },
    {
        "id": 2,
        "code_rule": "rm002",
        "clasic_test_min_porcentaje": 59,
        "virtual_task_min_porcentaje": 50,
        "msg_in_range" : "Se ha encontrado una posible deficiencia visual del color",
        "msg_out_range" : "No se ha encontrado una posible deficiencia visual del color"
    }
]

rules_ophthalmological_all_test = [
    {
        "id": 1,
        "total_min_value": 91,
        "total_max_value": 100,
        "msg": "No se han encontrado deficiencias visuales"
    },
    {
        "id": 2,
        "total_min_value": 81,
        "total_max_value": 90,
        "msg": "No se han encontrado deficiencias visuales importantes"
    },
    {
        "id": 3,
        "total_min_value": 61,
        "total_max_value": 80,
        "msg": "Tiene alguna deficiencia visual, es necesario acudir al especialista"
    },
    {
        "id": 4,
        "total_min_value": 31,
        "total_max_value": 60,
        "msg": "Tiene deficiencias visuales, debe acudir al especialista"
    },
    {
        "id": 5,
        "total_min_value": 10,
        "total_max_value": 30,
        "msg": "Tiene deficiencias visuales importantes, debe acudir al especialista"
    }
]