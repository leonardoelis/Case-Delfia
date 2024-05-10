import pandas as pd
from exceptions import InvalidFileStructureError, NonNumericValueError
import logging


def config_logs():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s %(name)s %(lineno)d %(levelname)s %(message)s')
    file_handler = logging.FileHandler('logs.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    try:
        logger = config_logs()
        df = pd.read_csv('transacoes.csv')

        print(df)
        if len(df.columns) != 3:
            raise InvalidFileStructureError('O arquivo fornecido apresenta problemas em sua estrutura. '
                                            f'O arquivo deve conter 3 colunas, porém ele possui {len(df.columns)} coluna(s).'
                                            f'\nLembre-se de utilizar vírgula (,) como separador no arquivo csv.')

        if not pd.api.types.is_numeric_dtype(df['Valor da Transação']):
            raise NonNumericValueError('A coluna "Valor da Transação" possui valores não numéricos')

        high_transactions = df[df['Valor da Transação'] > 1000]
        print(high_transactions)
        print(type(high_transactions))

        high_transactions.to_csv('transacoes_altas.csv', index=False)
    except (InvalidFileStructureError, NonNumericValueError) as e:
        print(e.message)
        logger.exception(e)
    except pd.errors.ParserError as e:
        print('Erro durante a leitura do arquivo CSV:', e)
        logger.exception(e)
    except Exception as e:
        print(e)
        logger.exception(e)
