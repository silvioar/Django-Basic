
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from random import randint
import pandas as pd
from django.shortcuts import render
import requests
import json
import pandas as pd
import time
import numpy as np
from core.homepage.functions import *



class DashboardView(TemplateView):

    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # Market Cap
    def get_mk(self):
        data = []
                  
        df = get_cripto_data()
        for i in range(0, len(df)):
            mk = df['market_cap'][i]
            crypto = df['moneda'][i]

            a = {'name': crypto, 'y': mk}
            data.append(a)
                
        return data

    
    # Mes
    def get_month(self): 
              
        fecha= datetime.now()        
        a = fecha.strftime("%b")           
        
        return a
    
    # Precios
    def get_prices(self): 
        
        df = get_cripto_data()
        precio_btc = df['precio'][df['moneda'] == 'bitcoin']
        precio_eth = df['precio'][df['moneda'] == 'ethereum']
        precio_link = df['precio'][df['moneda'] == 'chainlink']
        precio_ada = df['precio'][df['moneda'] == 'cardano']
        precio_dot = df['precio'][df['moneda'] == 'polkadot']
        precio_cro = df['precio'][df['moneda'] == 'crypto-com-chain']

        return float(precio_btc), float(precio_eth), float(precio_link), float(precio_ada), float(precio_dot), round(float(precio_cro),2)
    
    
    # Volumen 1
    def get_graph_3(self):     

        df = get_cripto_data()
        df = df.sort_values(["volumen"], ascending=False)
        monedas = list(df['moneda'])        
        
        return monedas

    # Volumen 2
    def get_graph_4(self):

        df = get_cripto_data()
        df = df.sort_values(["volumen"], ascending=False)
        precio = list(df['volumen'])

        return precio
            
    # Conexion con JS
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'        
        context['graph_3'] = self.get_graph_3()
        context['graph_4'] = self.get_graph_4()     
        context['month'] = self.get_month()   
        context['btc'] = self.get_prices()[0]  
        context['eth'] = self.get_prices()[1]
        context['link'] = self.get_prices()[2]  
        context['ada'] = self.get_prices()[3]  
        context['dot'] = self.get_prices()[4]  
        context['cro'] = self.get_prices()[5]  
        context['get_mk'] = self.get_mk()     

        return context


