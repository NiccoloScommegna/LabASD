from heap import Heap
from linked_list import LinkedList
from ordered_linked_list import OrderedLinkedList
from enums import DataType, ArrayType, ArraySize

from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt


def get_data_structure_type():
    print("Seleziona il tipo di struttura dati:")
    for i, data_type in enumerate(DataType, start=1):
        print(f"{i}. {data_type.value}")

    while True:
        try:
            choice = int(input("Inserisci il numero corrispondente: "))
            return list(DataType)[choice - 1]
        except (ValueError, IndexError):
            print("Scelta non valida. Inserisci un numero valido.")


def get_array_type():
    print("Seleziona il tipo di array:")
    for i, array_type in enumerate(ArrayType, start=1):
        print(f"{i}. {array_type.value}")

    while True:
        try:
            choice = int(input("Inserisci il numero corrispondente: "))
            return list(ArrayType)[choice - 1]
        except (ValueError, IndexError):
            print("Scelta non valida. Inserisci un numero valido.")


def get_array_size():
    print("Seleziona la dimensione dell'array:")
    for i, array_size in enumerate(ArraySize, start=1):
        print(f"{i}. {array_size.name} ({array_size.value} elementi)")

    while True:
        try:
            choice = int(input("Inserisci il numero corrispondente: "))
            return list(ArraySize)[choice - 1]
        except (ValueError, IndexError):
            print("Scelta non valida. Inserisci un numero valido.")


def create_data_structure(data_structure_type):
    if data_structure_type == DataType.HEAP:
        return Heap()
    elif data_structure_type == DataType.LINKED_LIST:
        return LinkedList()
    elif data_structure_type == DataType.ORDERED_LINKED_LIST:
        return OrderedLinkedList()


def create_numpy_array(array_type, array_size):
    if array_type == ArrayType.RANDOM:
        return np.random.randint(1, 100, size=array_size.value)
    elif array_type == ArrayType.ASCENDING:
        return np.arange(1, array_size.value + 1)
    elif array_type == ArrayType.DESCENDING:
        return np.arange(array_size.value, 0, -1)


def perform_insertion(my_data_structure, my_numpy_array, insertion_times_matrix, i):
    for j, value in enumerate(my_numpy_array):
        start_time = timer()
        my_data_structure.insert(value)
        end_time = timer()
        insertion_times_matrix[i, j] = end_time - start_time
        # In ogni riga salvo i tempi di inserimento secondo questa logica: [riga 0, colonna 0] = tempo di inserimento
        # del primo elemento, [riga 0, colonna 1] = tempo di inserimento del secondo elemento, fino a [riga 0,
        # colonna array_size] = tempo di inserimento dell'ultimo elemento. Il tutto fatto i volte (numero di test).
        # Poi nel main calcolo la media di ogni colonna e faccio il plot, così ho la media sul primo inserimento,
        # poi sul secondo e così via fino all'ultimo.
    return insertion_times_matrix


def perform_extraction(my_data_structure, my_numpy_array, extraction_times_matrix, i):
    for j in range(len(my_numpy_array)):
        start_time = timer()
        my_data_structure.extract_max()
        end_time = timer()
        extraction_times_matrix[i, j] = end_time - start_time
    return extraction_times_matrix


def plot_operation_times_small(x_values, y_values, data_structure_type, array_type, operation):
    ymax_value = 0.00002
    plt.figure()
    if operation == "Inserimento":
        plt.plot(x_values, y_values, label="Tempi di inserimento", color='b')
    else:
        plt.plot(x_values, y_values, label="Tempi di estrazione", color='g')
    plt.xlabel("Numero di operazioni effettuate")
    plt.ylabel("Tempo (secondi)")
    plt.grid(True)
    plt.title(f"{operation} - {data_structure_type.value} - input: {array_type.value}")
    plt.ylim(0, ymax_value)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    plt.tight_layout()

    plt.show()


def plot_operation_times_medium_by_data_structure(x_values, y_values_random, y_values_ascending, y_values_descending,
                                                  data_structure_type, operation):
    ymax_value = 0.00017
    plt.figure()

    plt.plot(x_values, y_values_random, label=f"Random")
    plt.plot(x_values, y_values_ascending, label=f"Ascending")
    plt.plot(x_values, y_values_descending, label=f"Descending")

    plt.xlabel("Numero di operazioni effettuate")
    plt.ylabel(f"Tempo (secondi)")
    plt.grid(True)
    plt.title(f"{operation} - {data_structure_type.value}")
    plt.legend()
    plt.ylim(0, ymax_value)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    plt.tight_layout()

    plt.show()


def plot_operation_times_medium_by_array_type(x_values, y_values_heap, y_values_linked_list,
                                              y_values_ordered_linked_list, array_type, operation):
    ymax_value = 0.00017
    plt.figure()

    plt.plot(x_values, y_values_heap, label=f"Heap")
    plt.plot(x_values, y_values_linked_list, label=f"Linked List")
    plt.plot(x_values, y_values_ordered_linked_list, label=f"Ordered Linked List")

    plt.xlabel("Numero di operazioni effettuate")
    plt.ylabel("Tempo (secondi)")
    plt.grid(True)
    plt.title(f"{operation} - input: {array_type.value}")
    plt.legend()
    plt.ylim(0, ymax_value)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    plt.tight_layout()

    plt.show()


def plot_operation_times_large(x_values, y_values_insertion, y_values_extraction, array_type, data_structure_type):
    ymax_value_heap = 0.00004
    ymax_value_linked_list = 0.00165
    ymax_value_ordered_linked_list = 0.00145
    plt.figure()

    plt.plot(x_values, y_values_insertion, label=f"Inserimento")
    plt.plot(x_values, y_values_extraction, label=f"Estrazione")

    plt.xlabel("Numero di operazioni effettuate")
    plt.ylabel("Tempo (secondi)")
    plt.grid(True)
    plt.title(f"{data_structure_type.value} - input: {array_type.value}")
    plt.legend()
    if data_structure_type == DataType.HEAP:
        plt.ylim(0, ymax_value_heap)
    elif data_structure_type == DataType.LINKED_LIST:
        plt.ylim(0, ymax_value_linked_list)
    else:
        plt.ylim(0, ymax_value_ordered_linked_list)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
    plt.tight_layout()

    plt.show()


def main():
    NUMBER_OF_TEST = 50  # Costante NUMBER_OF_TEST

    # Chiedi all'utente di selezionare l'array_size
    array_size = get_array_size()

    # Gestisci il flusso in base all'array_size
    if array_size == ArraySize.SMALL:
        # Chiedi all'utente di selezionare l'array_type
        array_type = get_array_type()
        print(f"Hai scelto come input: {array_type.value} e {array_size.value}.")

        # Esegue i test per ogni struttura dati e fa il plot di ogni misurazione
        for k, data_structure_type in enumerate([DataType.HEAP, DataType.LINKED_LIST, DataType.ORDERED_LINKED_LIST]):
            my_data_structure = create_data_structure(data_structure_type)
            my_numpy_array = create_numpy_array(array_type, array_size)

            # Inizializza le matrici numpy
            insertion_times_matrix = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix = np.zeros((NUMBER_OF_TEST, array_size.value))

            # Si esegue i test
            for i in range(NUMBER_OF_TEST):
                # Misura il tempo di inserimento degli elementi nella struttura dati
                insertion_times_matrix = perform_insertion(my_data_structure, my_numpy_array, insertion_times_matrix, i)

                # Misura il tempo di estrazione degli elementi dalla struttura dati
                extraction_times_matrix = perform_extraction(my_data_structure, my_numpy_array, extraction_times_matrix,
                                                             i)

            # Calcola le medie lungo le colonne
            average_insertion_times = np.mean(insertion_times_matrix, axis=0)
            average_extraction_times = np.mean(extraction_times_matrix, axis=0)

            # Crea il grafico per le medie dei tempi di inserimento
            plot_operation_times_small(range(1, array_size.value + 1), average_insertion_times, data_structure_type,
                                       array_type, "Inserimento")

            # Crea il grafico per le medie dei tempi di estrazione
            plot_operation_times_small(range(1, array_size.value + 1), average_extraction_times, data_structure_type,
                                       array_type, "Estrazione")

    elif array_size == ArraySize.MEDIUM:

        for k, data_structure_type in enumerate([DataType.HEAP, DataType.LINKED_LIST, DataType.ORDERED_LINKED_LIST]):
            my_data_structure = create_data_structure(data_structure_type)

            insertion_times_matrix_random = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_random = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_numpy_array = create_numpy_array(ArrayType.RANDOM, array_size)
                insertion_times_matrix_random = perform_insertion(my_data_structure, my_numpy_array,
                                                                  insertion_times_matrix_random, i)
                extraction_times_matrix_random = perform_extraction(my_data_structure, my_numpy_array,
                                                                    extraction_times_matrix_random, i)

            average_insertion_times_random = np.mean(insertion_times_matrix_random, axis=0)
            average_extraction_times_random = np.mean(extraction_times_matrix_random, axis=0)

            insertion_times_matrix_ascending = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_ascending = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_numpy_array = create_numpy_array(ArrayType.ASCENDING, array_size)
                insertion_times_matrix_ascending = perform_insertion(my_data_structure, my_numpy_array,
                                                                     insertion_times_matrix_ascending, i)
                extraction_times_matrix_ascending = perform_extraction(my_data_structure, my_numpy_array,
                                                                       extraction_times_matrix_ascending, i)

            average_insertion_times_ascending = np.mean(insertion_times_matrix_ascending, axis=0)
            average_extraction_times_ascending = np.mean(extraction_times_matrix_ascending, axis=0)

            insertion_times_matrix_descending = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_descending = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_numpy_array = create_numpy_array(ArrayType.DESCENDING, array_size)
                insertion_times_matrix_descending = perform_insertion(my_data_structure, my_numpy_array,
                                                                      insertion_times_matrix_descending, i)
                extraction_times_matrix_descending = perform_extraction(my_data_structure, my_numpy_array,
                                                                        extraction_times_matrix_descending, i)

            average_insertion_times_descending = np.mean(insertion_times_matrix_descending, axis=0)
            average_extraction_times_descending = np.mean(extraction_times_matrix_descending, axis=0)

            plot_operation_times_medium_by_data_structure(range(1, array_size.value + 1),
                                                          average_insertion_times_random,
                                                          average_insertion_times_ascending,
                                                          average_insertion_times_descending, data_structure_type,
                                                          "Inserimento")
            plot_operation_times_medium_by_data_structure(range(1, array_size.value + 1),
                                                          average_extraction_times_random,
                                                          average_extraction_times_ascending,
                                                          average_extraction_times_descending, data_structure_type,
                                                          "Estrazione")

        for k, array_type in enumerate([ArrayType.RANDOM, ArrayType.ASCENDING, ArrayType.DESCENDING]):
            my_numpy_array = create_numpy_array(array_type, array_size)

            insertion_times_matrix_heap = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_heap = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_data_structure = create_data_structure(DataType.HEAP)
                insertion_times_matrix_heap = perform_insertion(my_data_structure, my_numpy_array,
                                                                insertion_times_matrix_heap, i)
                extraction_times_matrix_heap = perform_extraction(my_data_structure, my_numpy_array,
                                                                  extraction_times_matrix_heap, i)

            average_insertion_times_heap = np.mean(insertion_times_matrix_heap, axis=0)
            average_extraction_times_heap = np.mean(extraction_times_matrix_heap, axis=0)

            insertion_times_matrix_linked_list = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_linked_list = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_data_structure = create_data_structure(DataType.LINKED_LIST)
                insertion_times_matrix_linked_list = perform_insertion(my_data_structure, my_numpy_array,
                                                                       insertion_times_matrix_linked_list, i)
                extraction_times_matrix_linked_list = perform_extraction(my_data_structure, my_numpy_array,
                                                                         extraction_times_matrix_linked_list, i)

            average_insertion_times_linked_list = np.mean(insertion_times_matrix_linked_list, axis=0)
            average_extraction_times_linked_list = np.mean(extraction_times_matrix_linked_list, axis=0)

            insertion_times_matrix_ordered_linked_list = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix_ordered_linked_list = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                my_data_structure = create_data_structure(DataType.ORDERED_LINKED_LIST)
                insertion_times_matrix_ordered_linked_list = perform_insertion(my_data_structure, my_numpy_array,
                                                                               insertion_times_matrix_ordered_linked_list,
                                                                               i)
                extraction_times_matrix_ordered_linked_list = perform_extraction(my_data_structure,
                                                                                 my_numpy_array,
                                                                                 extraction_times_matrix_ordered_linked_list,
                                                                                 i)

            average_insertion_times_ordered_linked_list = np.mean(insertion_times_matrix_ordered_linked_list, axis=0)
            average_extraction_times_ordered_linked_list = np.mean(extraction_times_matrix_ordered_linked_list, axis=0)

            plot_operation_times_medium_by_array_type(range(1, array_size.value + 1), average_insertion_times_heap,
                                                      average_insertion_times_linked_list,
                                                      average_insertion_times_ordered_linked_list, array_type,
                                                      "Inserimento")
            plot_operation_times_medium_by_array_type(range(1, array_size.value + 1), average_extraction_times_heap,
                                                      average_extraction_times_linked_list,
                                                      average_extraction_times_ordered_linked_list, array_type,
                                                      "Estrazione")

    else:  # array_size == ArraySize.LARGE

        data_structure_type = get_data_structure_type()
        print(f"Hai scelto come input: {data_structure_type.value} e {array_size.value}.")
        for k, array_type in enumerate([ArrayType.RANDOM, ArrayType.ASCENDING, ArrayType.DESCENDING]):
            my_numpy_array = create_numpy_array(array_type, array_size)
            my_data_structure = create_data_structure(data_structure_type)

            insertion_times_matrix = np.zeros((NUMBER_OF_TEST, array_size.value))
            extraction_times_matrix = np.zeros((NUMBER_OF_TEST, array_size.value))

            for i in range(NUMBER_OF_TEST):
                insertion_times_matrix = perform_insertion(my_data_structure, my_numpy_array,
                                                           insertion_times_matrix, i)
                extraction_times_matrix = perform_extraction(my_data_structure, my_numpy_array,
                                                             extraction_times_matrix, i)

            average_insertion_times = np.mean(insertion_times_matrix, axis=0)
            average_extraction_times = np.mean(extraction_times_matrix, axis=0)

            plot_operation_times_large(range(1, array_size.value + 1), average_insertion_times,
                                       average_extraction_times, array_type, data_structure_type)


# -----------------------------------Mean and Median-----------------------------------#
def perform_insertion_mean_median(my_data_structure, my_numpy_array):
    start_total_insertion_time = timer()
    for j, value in enumerate(my_numpy_array):
        my_data_structure.insert(value)

    end_total_insertion_time = timer()
    return end_total_insertion_time - start_total_insertion_time


def perform_extraction_mean_median(my_data_structure, my_numpy_array):
    start_total_extraction_time = timer()
    for j in range(len(my_numpy_array)):
        my_data_structure.extract_max()
    end_total_extraction_time = timer()
    return end_total_extraction_time - start_total_extraction_time


def mean_and_median():
    NUMBER_OF_TEST = 50
    array_size = get_array_size()

    for k, data_structure_type in enumerate([DataType.HEAP, DataType.LINKED_LIST, DataType.ORDERED_LINKED_LIST]):
        my_data_structure = create_data_structure(data_structure_type)
        my_numpy_array_random = create_numpy_array(ArrayType.RANDOM, array_size)

        total_insertion_times_array = np.zeros(NUMBER_OF_TEST)
        total_extraction_times_array = np.zeros(NUMBER_OF_TEST)

        for i in range(NUMBER_OF_TEST):
            total_insertion_times_array[i] = perform_insertion_mean_median(my_data_structure, my_numpy_array_random)
            total_extraction_times_array[i] = perform_extraction_mean_median(my_data_structure, my_numpy_array_random)

        # Calcolo del tempo medio per completare tutti gli inserimenti e tutte le estrazioni
        average_total_insertion_time = np.mean(total_insertion_times_array)
        average_total_extraction_time = np.mean(total_extraction_times_array)

        # Calcolo della mediana dei tempi totali di inserimento ed estrazione
        median_total_insertion_time = np.median(total_insertion_times_array)
        median_total_extraction_time = np.median(total_extraction_times_array)

        print(f"\n{data_structure_type.value} - Tipo di input {ArrayType.RANDOM.value}:")
        print(f"Tempo medio totale di inserimento: {average_total_insertion_time} secondi")
        print(f"Mediana dei tempi totali di inserimento: {median_total_insertion_time} secondi")
        print(f"Tempo medio totale di estrazione: {average_total_extraction_time} secondi")
        print(f"Mediana dei tempi totali di estrazione: {median_total_extraction_time} secondi")

        my_numpy_array_ascending = create_numpy_array(ArrayType.ASCENDING, array_size)

        total_insertion_times_array = np.zeros(NUMBER_OF_TEST)
        total_extraction_times_array = np.zeros(NUMBER_OF_TEST)

        for i in range(NUMBER_OF_TEST):
            total_insertion_times_array[i] = perform_insertion_mean_median(my_data_structure, my_numpy_array_ascending)
            total_extraction_times_array[i] = perform_extraction_mean_median(my_data_structure,
                                                                             my_numpy_array_ascending)

        # Calcolo del tempo medio per completare tutti gli inserimenti e tutte le estrazioni
        average_total_insertion_time = np.mean(total_insertion_times_array)
        average_total_extraction_time = np.mean(total_extraction_times_array)

        # Calcolo della mediana dei tempi totali di inserimento ed estrazione
        median_total_insertion_time = np.median(total_insertion_times_array)
        median_total_extraction_time = np.median(total_extraction_times_array)

        print(f"\n{data_structure_type.value} - Tipo di input {ArrayType.ASCENDING.value}:")
        print(f"Tempo medio totale di inserimento: {average_total_insertion_time} secondi")
        print(f"Mediana dei tempi totali di inserimento: {median_total_insertion_time} secondi")
        print(f"Tempo medio totale di estrazione: {average_total_extraction_time} secondi")
        print(f"Mediana dei tempi totali di estrazione: {median_total_extraction_time} secondi")

        my_numpy_array_descending = create_numpy_array(ArrayType.DESCENDING, array_size)

        total_insertion_times_array = np.zeros(NUMBER_OF_TEST)
        total_extraction_times_array = np.zeros(NUMBER_OF_TEST)

        for i in range(NUMBER_OF_TEST):
            total_insertion_times_array[i] = perform_insertion_mean_median(my_data_structure, my_numpy_array_descending)
            total_extraction_times_array[i] = perform_extraction_mean_median(my_data_structure,
                                                                             my_numpy_array_descending)

        # Calcolo del tempo medio per completare tutti gli inserimenti e tutte le estrazioni
        average_total_insertion_time = np.mean(total_insertion_times_array)
        average_total_extraction_time = np.mean(total_extraction_times_array)

        # Calcolo della mediana dei tempi totali di inserimento ed estrazione
        median_total_insertion_time = np.median(total_insertion_times_array)
        median_total_extraction_time = np.median(total_extraction_times_array)

        # if data_structure_type == DataType.LINKED_LIST:
        #     print(f"\n{data_structure_type.value} - Tipo di input {ArrayType.DESCENDING.value}:")
        #     print(total_insertion_times_array)

        print(f"\n{data_structure_type.value} - Tipo di input {ArrayType.DESCENDING.value}:")
        print(f"Tempo medio totale di inserimento: {average_total_insertion_time} secondi")
        print(f"Mediana dei tempi totali di inserimento: {median_total_insertion_time} secondi")
        print(f"Tempo medio totale di estrazione: {average_total_extraction_time} secondi")
        print(f"Mediana dei tempi totali di estrazione: {median_total_extraction_time} secondi")

        print("\n")


if __name__ == "__main__":
    main()
    # mean_and_median()

    # arr = np.array([9, 4, 7, 2, 5, 11, 1, 8, 3, 6])
    # arr = np.arange(10, 0, -1)
    # print(arr)

    # heap = Heap()
    # for value in arr:
    #     heap.insert(value)
    #     heap.display_tree()
    # heap.print_heap()
    # heap.display_tree()
    # heap_max_value = heap.extract_max()
    # print("Max value:", heap_max_value)
    # heap.print_heap()

    # linked_list = LinkedList()
    # for value in arr:
    #     linked_list.insert(value)
    # linked_list.print_list()
    # linked_list_max_value = linked_list.extract_max()
    # print("Max value:", linked_list_max_value)
    # linked_list.print_list()

    # ordered_linked_list = OrderedLinkedList()
    # for value in arr:
    #     ordered_linked_list.insert(value)
    # ordered_linked_list.print_list()
    # ordered_linked_list_max_value = ordered_linked_list.extract_max()
    # print("Max value:", ordered_linked_list_max_value)
    # ordered_linked_list.print_list()
