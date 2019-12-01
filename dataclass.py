fro dataclasses import dataclass, field, InitVar
from typing import List, Any,Callable, ClassVar, Dict, Optional
from contextlib import ContextDecorator

@dataclass
class MyClass(ContextDecorator):
    text: str = None
    name: str = None
    name_dict: ClassVar[Dict[str, int]] = dict()
    names: List[str] = field(default_factory=list)
    timer: Optional[float] = field(default=0, init=False, repr=False)
    
    def __post_init__(self):
        if self.name:
            if self.name in self.name_dict:
                self.name_dict[self.name] += 1
            else:
                self.name_dict[self.name] = 0
            self.names.append(self.name)
            
    def __enter__(self):
        print("enter!")
        return self
    
    def __exit__(self, *exc_info):
        print("exit!")
            
if __name__ == '__main__':
    m = MyClass(name="Hsin")
    print(m.names)
    
    with MyClass('Hsin') as m:
    print(m.name_dict)
    
    @MyClass('hsin')
    def myfunc():
        pass
    
    myfunc()
    
