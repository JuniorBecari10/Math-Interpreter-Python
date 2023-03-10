from nodes import *
from values import Number
import util

class Interpreter:
  def visit(self, node):
    method_name = f"visit_{type(node).__name__}"
    # ex.: AddNode -> visit_AddNode
    
    method = getattr(self, method_name)
    return method(node)
  
  def visit_NumberNode(self, node):
    return Number(node.value)
  
  def visit_AddNode(self, node):
    return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)
  
  def visit_SubtractNode(self, node):
    return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)
  
  def visit_MultiplyNode(self, node):
    return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)
  
  def visit_DivideNode(self, node):
    try:
      return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
    except Exception:
      util.print_error(None, "Cannot divide by zero.")
  
  def visit_PlusNode(self, node):
    return self.visit(node.node).value
  
  def visit_MinusNode(self, node):
    return Number(-self.visit(node.node).value)