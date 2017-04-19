'''
Created on Apr 12, 2017

@author: jrm
'''
from atom.api import (
    Event, List, Value, Unicode, Dict, Instance, Bool
)

from enaml.core.declarative import d_

from enaml.widgets.toolkit_object import ToolkitObject

class Tag(ToolkitObject):
    #: Object ID
    id = d_(Unicode())
    
    #: Tag name (leave blank for class name)
    tag = d_(Unicode())
    
    #: CSS classes
    cls = d_(Instance((list,basestring)))
    
    #: CSS styles
    style = d_(Instance((dict,basestring)))
    
    #: Node text
    text = d_(Unicode())
    
    #: Title attribute
    #title = d_(Unicode())
    
    #: Alt attribute
    alt = d_(Unicode())    
    
    #: Custom attributes not explicityl defined
    attrs = d_(Dict())
        
class Html(Tag):
    def render(self, parent=None):
        if not self.is_initialized:
            self.initialize()
        if not self.proxy_is_active:
            self.activate_proxy()
        return self.proxy.render()
    
class Head(Tag):
    pass    

class Body(Tag):
    pass    

class Title(Tag):
    pass    

class P(Tag):
    pass

class H1(Tag):
    pass

class H2(Tag):
    pass           

class H3(Tag):
    pass

class H4(Tag):
    pass

class H5(Tag):
    pass

class H6(Tag):
    pass

class Hr(Tag):
    pass

class Br(Tag):
    pass

class Pre(Tag):
    pass

class Code(Tag):
    pass

class Kbd(Tag):
    pass

class Samp(Tag):
    pass

class Var(Tag):
    pass

class Div(Tag):
    pass

class Span(Tag):
    pass                    

class A(Tag):
    href = d_(Unicode())
    target = d_(Unicode())#Enum("_blank","_self","_parent","_top","framename"))
    
class B(Tag):
    pass

class I(Tag):
    pass

class Strong(Tag):
    pass

class Em(Tag):
    pass

class Mark(Tag):
    pass

class Small(Tag):
    pass

class Del(Tag):
    pass

class Ins(Tag):
    pass

class Sub(Tag):
    pass

class Sup(Tag):
    pass

class Q(Tag):
    pass

class Blockquote(Tag):
    cite = d_(Unicode())

class Abbr(Tag):
    pass

class Address(Tag):
    pass

class Cite(Tag):
    pass

class Bdo(Tag):
    dir = d_(Unicode())

class Img(Tag):
    src = d_(Unicode())
    width = d_(Unicode())
    height = d_(Unicode())            

class Style(Tag):
    pass

class Link(Tag):
    type = d_(Unicode())
    rel = d_(Unicode())
    href = d_(Unicode())
    rel = d_(Unicode())
    media = d_(Unicode())
    
class Map(Tag):
    name = d_(Unicode())

class Area(Tag):
    shape = d_(Unicode())
    coords = d_(Unicode())
    href = d_(Unicode())
    
class Table(Tag):
    pass

class Tr(Tag):
    pass

class Td(Tag):
    pass

class Th(Tag):
    colspan = d_(Unicode())
    rowspan = d_(Unicode())

class THead(Tag):
    pass

class TBody(Tag):
    pass

class TFoot(Tag):
    pass

class Caption(Tag):
    pass
    
class Ul(Tag):
    pass

class Ol(Tag):
    type = d_(Unicode())#Enum("1","A","a","I","i"))

class Li(Tag):
    pass

class Dl(Tag):
    pass

class Dt(Tag):
    pass

class Dd(Tag):
    pass

class IFrame(Tag):
    src = d_(Unicode())
    height = d_(Unicode())
    width = d_(Unicode())
    target = d_(Unicode())
    
class Script(Tag):
    src = d_(Unicode())
    type = d_(Unicode())

class NoScript(Tag):
    pass

class Meta(Tag):
    name = d_(Unicode())
    content = d_(Unicode())
    
class Base(Tag):
    href = d_(Unicode())
    target = d_(Unicode())#Enum("_blank","_self","_parent","_top","framename"))
    
class Header(Tag):
    pass

class Nav(Tag):
    pass

class Section(Tag):
    pass

class Aside(Tag):
    pass

class Article(Tag):
    pass

class Footer(Tag):
    pass

class Summary(Tag):
    pass

class Details(Tag):
    pass

class Form(Tag):
    action = d_(Unicode())
    method = d_(Unicode())#Enum("get","post"))
    
class Fieldset(Tag):
    pass

class Legend(Tag):
    pass

class Label(Tag):
    pass

class Select(Tag):
    name = d_(Unicode())
    value = d_(Unicode())
    
class Option(Tag):
    value = d_(Unicode())

class Input(Tag):
    name = d_(Unicode())
    type = d_(Unicode())#Enum("radio","checkbox","text","hidden","submit"))
    disabled = d_(Bool())
    checked = d_(Bool())
    value = d_(Value())
    
class Textarea(Tag):
    name = d_(Unicode())
    rows = d_(Unicode())
    cols = d_(Unicode())
    
class Button(Tag):
    type=d_(Unicode())
    onclick = d_(Event())
    