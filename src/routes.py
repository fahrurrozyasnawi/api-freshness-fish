from controller import ClassifyFish, FreshnessClassify, Classify

def init_routes(api):
  api.add_resource(ClassifyFish, '/fish')
  api.add_resource(FreshnessClassify, '/freshness')
  api.add_resource(Classify, '/results')