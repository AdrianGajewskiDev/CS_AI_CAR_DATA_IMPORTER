import json
from typing import List
from data_importer.aws.dynamo_db import save_data_to_dynamo_db
from data_importer.logging.internal_logger import InternalLogger


def save_data(event: dict) -> int:
    data = event.get("data")

    if not data:
        raise ValueError("No data provided")
    table_items = []
    for key, value in data.items():
        partition_key = key
        InternalLogger.LogInfo(f"Partition_Key: {partition_key}")
        for sub_key, sub_value in value.items():
            InternalLogger.LogInfo(f"Sort_key: {sub_key}")

            generations = "[]"

            if isinstance(sub_value, dict):
                generations = build_generations(sub_value)
            
            table_items.append({"make": partition_key, "model": sub_key, "generations": generations})

    for item in table_items:
        InternalLogger.LogInfo(f"Item: {item}")
        save_data_to_dynamo_db(item["make"], item["model"], item["generations"])

    return len(table_items)

def build_generations(generations: List[dict]) -> str:
    build_gen = lambda key, value: {"model": key, "years": value}
    _gens = [build_gen(key, value) for key, value in generations.items()]

    return json.dumps([gen for gen in _gens])

{
  "BMW Models": {
    "1 Series": {
      "E81": "2004-2011",
      "E87": "2004-2011",
      "E82": "2007-2013",
      "E88": "2007-2013",
      "F20": "2011-2019",
      "F21": "2011-2019",
      "F40": "2019-present"
    },
    "2 Series": {
      "F22": "2014-2021",
      "F23": "2014-present",
      "F45": "2014-present",
      "F46": "2014-present",
      "G42": "2021-present"
    },
    "3 Series": {
      "E21": "1975-1983",
      "E30": "1982-1994",
      "E36": "1990-2000",
      "E46": "1998-2006",
      "E90": "2005-2013",
      "E91": "2005-2012",
      "E92": "2006-2013",
      "E93": "2006-2013",
      "F30": "2011-2019",
      "F31": "2012-2019",
      "F34": "2013-2019",
      "G20": "2018-present",
      "G21": "2018-present",
      "G28": "2019-present"
    },
    "4 Series": {
      "F32": "2013-2020",
      "F33": "2013-2020",
      "F36": "2013-2020",
      "G22": "2020-present",
      "G23": "2020-present",
      "G26": "2021-present"
    },
    "5 Series": {
      "E12": "1972-1981",
      "E28": "1981-1988",
      "E34": "1987-1996",
      "E39": "1995-2004",
      "E60": "2003-2010",
      "E61": "2003-2010",
      "F10": "2010-2017",
      "F11": "2010-2017",
      "F07": "2009-2017",
      "G30": "2016-present",
      "G31": "2017-present",
      "G38": "2017-present"
    },
    "6 Series": {
      "E24": "1976-1989",
      "E63": "2003-2010",
      "E64": "2003-2010",
      "F06": "2011-2018",
      "F12": "2011-2018",
      "F13": "2011-2018"
    },
    "7 Series": {
      "E23": "1977-1986",
      "E32": "1986-1994",
      "E38": "1994-2001",
      "E65": "2001-2008",
      "E66": "2001-2008",
      "F01": "2008-2015",
      "F02": "2008-2015",
      "G11": "2015-present",
      "G12": "2015-present"
    },
    "8 Series": {
      "E31": "1990-1999",
      "G14": "2018-present",
      "G15": "2018-present",
      "G16": "2018-present"
    },
    "X1": {
      "E84": "2009-2015",
      "F48": "2015-2022",
      "U11": "2022-present"
    },
    "X2": {
      "F39": "2018-present"
    },
    "X3": {
      "E83": "2003-2010",
      "F25": "2010-2017",
      "G01": "2017-present"
    },
    "X4": {
      "F26": "2014-2018",
      "G02": "2018-present"
    },
    "X5": {
      "E53": "1999-2006",
      "E70": "2006-2013",
      "F15": "2013-2018",
      "G05": "2018-present"
    },
    "X6": {
      "E71": "2008-2014",
      "F16": "2014-2019",
      "G06": "2019-present"
    },
    "X7": {
      "G07": "2018-present"
    }
  }
}