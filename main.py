from multiprocessing.pool import ThreadPool

from db_fetch_stream.transfer_to_stream import commence
from db_fetch_stream.utilities import databases_helper


def main():
    database_list = databases_helper.get_db_list()

    pool = ThreadPool(len(database_list))
    pool.map(commence, database_list)

if __name__ == '__main__':
    main()
