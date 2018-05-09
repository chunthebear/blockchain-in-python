import hashlib
import json
from time import time
from uuid import uuid4


class Blockchain:
	#initiate genesis block
	def __init__(self):
	
		#use list to store chain of blocks
		self.chain=[]
		
		#use list to store transactions
		self.current_transactions=[]
		
		#create genesis block
		self.new_block(previous_hash=1, proof=100)
		
	#create a new block in chain
	def new_block(self, proof, previous_hash=None):
		#use dictinary to store properties for a new block
		block={
			'index': len(self.chain)+1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			
			#by proof of work algorithm
			'proof': proof,
			
			'previous_hash': previous_hash or self.hash(self.chain[-1])),
		}
		#reset current list of transactions
		self.current_transactions=[]

		self.chain.append(block)
		return block
		
	#record new transactions into list
	def new_transaction(self):
	
		#use dictionary to store new transactions
		#and append them in list into new block 
		self.current_transactions.append({
		
			#adress of sender
			'sender': sender,
			
			#address of recipient
			'recipient': recipient,
			
			#amount
			'amount': amount,
		})
		#return the index the block where these transactions are added to
		#it is also the next one to be mined
		return self.last_block['index'] + 1
	
	#hash a block
	@staticmethod
	def hash(block):
		#use libraries to encode SHA-256 hash for a block, which is converted to a string
		#make sure the dictionary 'block' is sorted
		block_key = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_key).hexdigest()

	@property
	def last_block(self):
		return self.chain[-1]
		
	def proof_of_work(self, last_proof):
		proof=0
		