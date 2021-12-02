#class ChooChoo(init_x, init_y, init_dir):
class ChooChoo:
	def __init__(self, init_x, init_y, init_dir):
		self.x = init_x
		self.y = init_y
		self.dir = init_dir
		self.next_turn = 'left'

	def step(self):
		if self.dir == '^':
			self.y -= 1
		elif self.dir == 'v':
			self.y += 1
		elif self.dir == '<':
			self.x -= 1
		elif self.dir == '>':
			self.x += 1
		return [self.x, self.y]

	def status(self):
		return [[self.x, self.y], self.dir, self.next_turn]
	
	def turn(self, junction):
		if junction == '/':
			self.dir = self._curveL(self.dir)
		elif junction == '⧵':
			self.dir = self._curveR(self.dir)
		elif junction == '+':
			self.dir, self.next_turn = self._intersection(self.dir, self.next_turn)
		return self.dir

	@staticmethod
	def _curveL(dir):
		if dir == '^':
			return '>'
		elif dir == 'v':
			return '<'
		elif dir == '<':
			return 'v'
		elif dir == '>':
			return '^'
	
	@staticmethod
	def _curveR(dir):
		if dir == '^':
			return '<'
		elif dir == 'v':
			return '>'
		elif dir == '<':
			return '^'
		elif dir == '>':
			return 'v'

	@staticmethod
	def _intersection(dir, next_turn):
		if next_turn == 'left':
			if dir == '^':
				return ['<', 'straight']
			elif dir == 'v':
				return ['>', 'straight']
			elif dir == '<':
				return ['v', 'straight']
			elif dir == '>':
				return ['^', 'straight']
		elif next_turn == 'right':
			if dir == '^':
				return ['>', 'left']
			elif dir == 'v':
				return ['<', 'left']
			elif dir == '<':
				return ['^', 'left']
			elif dir == '>':
				return ['v', 'left']
		elif next_turn == 'straight':
			return [dir, 'right']
