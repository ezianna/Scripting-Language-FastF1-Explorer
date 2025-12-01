import fastf1
fastf1.Cache.enable_cache('cache')

def load_session(year, gp, session):
    ses = fastf1.get_session(year, gp, session)
    ses.load()
    return ses
