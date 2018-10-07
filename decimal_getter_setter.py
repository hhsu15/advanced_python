from decimal import Decimal, ROUND_UP
class BankTransaction(object):
	_cents = Decimal('0.1')
	def __init__(self, account, before, after, min, max):
		self.account = account
		self._before = before
		self._after = after
		self._min = min
		self._max = max

	@property
	def before(self):
		return Decimal(self._before).quantize(self._cents, ROUND_UP)
	
	@before.setter
	def before(self, val):
		self._before = str(val)
