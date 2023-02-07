from tokens import *
from nodes import *

class Parser:
  def __init__(self, tokens):
    self.tokens = tokens
    self.cursor = 0
    self.tk = self.tokens[self.cursor]
  
  def next_token(self):
    self.cursor += 1
    self.tk = self.tokens[self.cursor] if self.cursor < len(self.tokens) else None
  
  def parse(self):
    if self.tk == None:
      return None
    
    res = self.term()
    
    while self.tk != None and self.tk.type in (TokenType.PLUS, TokenType.MINUS):
      if self.tk.type == TokenType.PLUS:
        self.next_token()
        
        res = AddNode(res, self.term())
      
      elif self.tk().type == TokenType.MINUS:
        self.next_token()
        
        res = SubtractNode(res, self.term())
    
    return res
  
  def term(self):
    res = self.factor()
    
    while self.tk != None and self.tk.type in (TokenType.TIMES, TokenType.DIVIDE):
      if self.tk.type == TokenType.TIMES:
        self.next_token()
        
        res = MultiplyNode(res, self.factor())
      
      elif self.tk.type == TokenType.DIVIDE:
        self.next_token()
        
        res = DivideNode(res, self.factor())
    
    return res
  
  def factor(self):
    if self.tk.type == TokenType.NUM:
      tk = self.tk
      self.next_token()
      
      return NumberNode(tk.value)