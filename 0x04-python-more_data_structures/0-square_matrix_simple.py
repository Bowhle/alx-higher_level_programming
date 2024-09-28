#!/usr/bin/python3
from typing import List, Any

def search_replace(my_list: List[Any], search: Any, replace: Any) -> List[Any]:
    return [replace if item == search else item for item in my_list]
