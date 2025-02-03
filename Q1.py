from qiskit import QuantumCircuit
circuit = QuantumCircuit(26)
count_number=0
while count_number!=(2**25):
	count_number = int(count_number)
	QuantumCircuit(count_number)
	count_number+=1
	count_number_save=count_number
	count_number_save-=1
	#print(count_number_save)
                                           