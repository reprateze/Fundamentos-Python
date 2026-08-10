from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    vetor = [1, 2, 3, 4]

    # divide em duas partes
    parte1 = vetor[:2]   # [1,2]
    parte2 = vetor[2:]   # [3,4]

    # envia parte2 para o processo 1
    comm.send(parte2, dest=1)

    # calcula soma da sua parte
    soma1 = sum(parte1)

    # recebe soma do processo 1
    soma2 = comm.recv(source=1)

    total = soma1 + soma2
    print("Soma total:", total)

else:
    # recebe parte do mestre
    dados = comm.recv(source=0)

    soma = sum(dados)

    # envia resultado de volta
    comm.send(soma, dest=0)