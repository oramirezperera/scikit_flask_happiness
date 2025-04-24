from utils import  Utils

def load_data(path):
    utils = Utils()
    data = utils.load_from_csv(path)
    countries = data['country'].tolist()
    X, y = utils.features_target(data, ['score', 'rank', 'country'], ['score'])
    country_score = data['score'].tolist()

    return X, y, countries, country_score