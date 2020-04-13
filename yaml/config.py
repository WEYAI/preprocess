import confuse
import namedtupled

config = confuse.Configuration("wueeryong" ,"config")
config.set_file("../config/config/yaml")
dic_config = config['ner'].get()
obj_config = namedtupled.map(dic_config)
