class Automacao():

    def ObterSinalAnalogico():
        import board
        import busio
        import adafruit_ads1x15.ads1115 as ADS
        import RPi.GPIO as GPIO
        from adafruit_ads1x15.analog_in import AnalogIn
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        chan = AnalogIn(ads, ADS.P0)
        return(chan.value)
    

    def MedirUmidadeDoSolo():
    
        valor_max_sensor_umidade = 26000
        valor_min_sensor_umidade = 11000
        percentual = 0
        valor_sinal_analogico = Automacao.ObterSinalAnalogico()
        
        diferença_valor_max_min = valor_max_sensor_umidade - valor_min_sensor_umidade #17000
        mediaValorMinMax = diferença_valor_max_min/2
            
        pontoMedio = (valor_max_sensor_umidade + valor_min_sensor_umidade)/2 #17500
        mediaPontoMedio = pontoMedio/2
        
        if(valor_sinal_analogico <= pontoMedio):
        
            if(valor_sinal_analogico < valor_min_sensor_umidade):
                valor_sinal_analogico = valor_min_sensor_umidade
                
            diferencaPontoMedio_sinalAnalogico = pontoMedio - valor_sinal_analogico
            valor_equivalente_analog =  mediaValorMinMax - diferencaPontoMedio_sinalAnalogico
            percentual = 100-((valor_equivalente_analog * 100) / diferença_valor_max_min)
    
        elif(valor_sinal_analogico >= pontoMedio):
            if(valor_sinal_analogico > valor_max_sensor_umidade):
                valor_sinal_analogico = valor_max_sensor_umidade
            
            diferencaSinalAnalogico_ValorMax = valor_max_sensor_umidade - valor_sinal_analogico
            valor_equivalente_analog =  diferença_valor_max_min - diferencaSinalAnalogico_ValorMax
            percentual = 100-((valor_equivalente_analog * 100) / diferença_valor_max_min)
   
        return round(percentual/100,2)

    def AcionarRele(binario,sleep):
        import RPi.GPIO as GPIO
        # Configuração das GPIOs (BCM)]
        GPIO.setwarnings(False)
        pino_rele_1 = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pino_rele_1, GPIO.OUT)
        GPIO.output(pino_rele_1,binario)
        
        if(binario == 1):
            time.sleep(sleep)
            GPIO.output(pino_rele_1,0)             




