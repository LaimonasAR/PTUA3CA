from typing import Any

def check_arguments(mandatory: Any, *args, **kwargs) -> None:
    print (mandatory)
    if args:
        print (args)
    if kwargs:
        print (kwargs)


check_arguments(1,2,3,4, name="Laimonas")