from web3 import Web3

from binance.client import Client
import asyncio

global rpc
rpc=""
global privKey
privKey=""
global betAmount
betAmount=0
global contract
contract=""

global lines
lines=[]

global abi
abi=[{"inputs":[{"internalType":"uint256","name":"asset","type":"uint256"},{"internalType":"uint256","name":"mins","type":"uint256"},{"internalType":"address","name":"ref","type":"address"}],"name":"goBear","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"asset","type":"uint256"},{"internalType":"uint256","name":"mins","type":"uint256"},{"internalType":"address","name":"ref","type":"address"}],"name":"goBull","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"hasGame","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isEvaluated","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"isWin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"readGame","outputs":[{"components":[{"internalType":"bool","name":"isReal","type":"bool"},{"internalType":"uint256","name":"assetId","type":"uint256"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"betAmount","type":"uint256"},{"internalType":"bool","name":"bull","type":"bool"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"minutesToPlay","type":"uint256"},{"internalType":"bool","name":"evaluated","type":"bool"},{"internalType":"bool","name":"refunded","type":"bool"},{"internalType":"bool","name":"won","type":"bool"},{"internalType":"uint256","name":"extensionCounter","type":"uint256"}],"internalType":"structzxBSC.gameTx","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"readUsersGame","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]

global contractInstance
global w3
async def instantiateContract():
	global contractInstance
	global w3
	global rpc
	global contract
	global abi
	w3=Web3(rpc)
	contractInstance= w3.eth.contract(address=contract, abi=abi)
	print("Contract instantiated.")

async def readConfig():
	global rpc
	global privKey
	global betAmount
	global contract

	with open('config.txt') as f:
	    lines = [line.rstrip().split("=")[1] for line in f]

	contract=lines[0]
	rpc=lines[1]
	privKey=lines[2]
	betAmount=lines[3]
	await instantiateContract()

asyncio.get_event_loop().run_until_complete(readConfig())
