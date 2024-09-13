from data_importer.save_data import save_data


def handler(event, context):
    return save_data(event)