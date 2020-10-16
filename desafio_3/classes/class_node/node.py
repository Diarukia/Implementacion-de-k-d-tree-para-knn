import pandas as pd
import numpy as np
import re
import copy


class _node:
    def __init__(self,id,track_name,size_bytes,currency,price,ratingcounttot,ratingcountver,user_rating,userratingver,
    ver,cont_rating,prime_genre,sup_devices_num,ipadSc_urls_num,lang_num,vpp_lic,df_row,genre_dict,depth):
        self.id = id
        self.track_name = track_name
        self.size_bytes = size_bytes
        self.currency = currency
        self.price = price
        self.ratingcounttot = ratingcounttot
        self.ratingcountver = ratingcountver
        self.user_rating = user_rating
        self.userratingver = userratingver
        self.ver = ver
        self.cont_rating = cont_rating
        self.prime_genre = prime_genre # se usara un numero para los generos
        self.sup_devices_num = sup_devices_num
        self.ipadSc_urls_num = ipadSc_urls_num
        self.lang_num = lang_num
        self.vpp_lic = vpp_lic # 16 parametros
        self.izq = None
        self.der = None
        self.depth = depth
        self.df_row = df_row
        del self.df_row["track_name"]
        del self.df_row["currency"]
        del self.df_row["ver"]
        self.df_row = self.df_row.replace(self.df_row.iloc[[0][0]][9],self.prime_genre)

    @staticmethod
    def create_node_charge_data(df_row,genre_dict,depth):
        return _node(df_row.iloc[0][1],df_row.iloc[0][2],df_row.iloc[0][3],df_row.iloc[0][4],df_row.iloc[0][5]
        ,df_row.iloc[0][6],df_row.iloc[0][7],df_row.iloc[0][8],df_row.iloc[0][9],df_row.iloc[0][10]
        ,float(df_row.iloc[0][11][0]),genre_dict[df_row.iloc[0][12]],df_row.iloc[0][13],df_row.iloc[0][14],df_row.iloc[0][15]
        ,df_row.iloc[0][16],df_row,genre_dict,depth)







