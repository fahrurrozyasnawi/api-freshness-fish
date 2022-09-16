from controller import ClassifyFish, FreshnessClassify

def init_routes(api):
  api.add_resource(ClassifyFish, '/fish')
  api.add_resource(FreshnessClassify, '/freshness')