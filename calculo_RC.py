# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
try: 
    len(base)
    print("si")
except:
    base=pd.read_csv("D:\\IDSS3399\\OneDrive - Comision Nacional Bancaria y de Valores\\Escritorio\\python\\RO_IC_BD.csv")
    base_pi=pd.read_csv("D:\IDSS3399\OneDrive - Comision Nacional Bancaria y de Valores\Escritorio\python\Perdida_riesgo_operacional_2811_gasto.csv")
    base_pi_a=pd.read_csv("D:\IDSS3399\OneDrive - Comision Nacional Bancaria y de Valores\Escritorio\python\Perdida_riesgo_operacional_A_2813_gasto.csv")
class calculo_IN:
    #definimos las variables que ocuparemos durante toda la clase
    def __init__(self,periodo,institucion,saldo,modelo):
        self.peri=periodo
        self.inst=institucion
        self.saldo=saldo
        self.modelo=modelo
    def periodos(self):
        #Esta funcion nos ayuda a obtener  los periodos que ocuparemos para poder realizar nuestros calculos
        self.peri_t=int(str(self.peri)[-2:])
        self.peri_1=self.peri-100+(12-int(str(self.peri-100)[-2:]))
        #
        self.peri_1_1=self.peri-100+1
        self.peri_2=self.peri-200+(12-int(str(self.peri-200)[-2:]))
        self.peri_2_1=self.peri-200+1
        self.peri_3=self.peri-300+(12-int(str(self.peri-300)[-2:]))
        self.peri_3_1=self.peri-300+1
        #
    def ob_base(self, periodo):
        #Esta funcion nos ayudara a filtrar nuestra base para obtener nuestros datos
        self.base=base.query("cve_institucion==@self.inst and cve_periodo==@periodo and cve_tipo_saldo==@self.saldo")
    def ob_base_ac(self, periodo):
        #Esta funcion nos ayudara a filtrar nuestros datos para obtener nuestros datos de activos productivos
        peri_a=periodo-int(str(periodo)[-2:])+1
        self.base_ac=base.query("cve_institucion==@self.inst and cve_periodo>=@peri_a and cve_periodo<=@periodo and cve_tipo_saldo==@self.saldo")
    def extraccion(self,num):
        #Esta funcion nos ayudara a obtener nuestro dato
        try:
            ex=self.base.query("cve_concepto==@num").iloc[0][11]
        except:
            ex=0
        return ex
    def extraccion_ac(self,num):
        #Esta funcion nos ayudara a obtener nuestros datos de activos productivos
        try:
            ex=sum(self.base_ac.query("cve_concepto==@num")["dat_importe"])
        except:
            ex=0
        return ex
    #Las siguientes funciones son para obtener nuestro dato requerido para cada calculo
    def ingresos_interes_22(self):
        #>2022
        #Intereses de cartera de crédito con riesgo de crédito etapa 1
        a1=self.extraccion(500200102008)
        # Intereses de cartera de crédito con riesgo de crédito etapa 2
        a2=self.extraccion(500200102009)
        # Intereses de cartera de crédito con riesgo de crédito etapa 3
        b=self.extraccion(500200102010)
        # Intereses y rendimientos a favor provenientes de inversiones en instrumentos financieros
        c=self.extraccion(500200102004)
        # Intereses y rendimientos a favor en operaciones de reporto
        d=self.extraccion(500200102005)
        # Intereses de efectivo y equivalentes de efectivo
        e=self.extraccion(500200102001)
        # Comisiones por el otorgamiento del crédito
        f=self.extraccion(500200102013)
        # Premios a favor en operaciones de préstamo de valores
        g=self.extraccion(500200102015)
        # Primas por colocación de deuda
        h=self.extraccion(500200102016)
        # Intereses y rendimientos a favor provenientes de cuentas de margen
        i=self.extraccion(500200102002)
        # Ingresos provenientes de operaciones de cobertura
        j=self.extraccion(500200102006)
        # Utilidad por valorización
        k=self.extraccion(500200102018)
        # Incremento por actualización de ingresos por intereses (1)
        l=self.extraccion(500200102019)
        # Ingresos por arrendamiento
        m=self.extraccion(501600802108)
        # Recuperación de cartera de crédito
        n=self.extraccion(600800402041)
        n=abs(n)
        i_p_i=a1+a2+b+c+d+e+f+g+h+i+j+k+l+m+n
        return i_p_i
    def ingresos_interes_20(self):
        #<2022
        #a. Intereses de cartera de crédito vigente
        a=self.extraccion(510500000000)
        # b. Intereses de cartera de crédito vencida
        b=self.extraccion(510200000000)
        # c. Intereses y rendimientos a favor provenientes de inversiones en valores
        c=self.extraccion(510300000000)
        # d. Intereses y rendimientos a favor en operaciones de reporto
        d=self.extraccion(510400000000)
        # e. Intereses de disponibilidades
        e=self.extraccion(510100000000)
        # f. Comisiones por el otorgamiento del crédito
        f=self.extraccion(510600000000)
        # g. Premios a favor en operaciones de préstamo de valores
        g=self.extraccion(510700000000)
        # h. Premios por colocación de deuda
        h=self.extraccion(511100000000)
        # i. Intereses y rendimientos a favor provenientes de cuentas de margen
        i=self.extraccion(511200000000)
        # j. Ingresos provenientes de operaciones de cobertura
        j=self.extraccion(511900000000)
        # k. Utilidad por valorización
        k=self.extraccion(510800000000)
        # l. Incremento por actualización de ingresos por intereses
        l=self.extraccion(519900000000)
        # m. Ingresos por arrendamiento
        m=self.extraccion(505032000000)
        i_p_i=a+b+c+d+e+f+g+h+i+j+k+l+m
        return i_p_i
    def gastos_intereses_22(self):
        #>2022
        # Intereses por depósitos de exigibilidad inmediata
        a=self.extraccion(600400202020)
        # Intereses por depósitos a plazo
        b=self.extraccion(600400202021)
        #"Intereses, costos de transacción y descuentos a cargo por emisión de instrumentos financieros que califican como pasivo"
        c=self.extraccion(600400202023)
        # Intereses por préstamos interbancarios y de otros organismos
        d=self.extraccion(600400202022)
        # Intereses y rendimientos a cargo en operaciones de reporto
        e=self.extraccion(600400202026)
        # Premios a cargo en operaciones de préstamo de valores
        f=self.extraccion(600400202029)
        # Costos y gastos asociados con el otorgamiento del crédito
        g=self.extraccion(600400202031)
        # Gastos provenientes de operaciones de cobertura
        h=self.extraccion(600400202027)
        # Pérdida por valorización
        i=self.extraccion(600400202032)
        # Intereses a cargo asociados con la cuenta global de captación sin movimientos
        j=self.extraccion(600400202033)
        # Incremento por actualización de gastos por intereses (1)
        k=self.extraccion(600400202036)
        g_p_i=a+b+c+d+e+f+g+h+i+j+k
        return g_p_i
    def gastos_intereses_20(self):
        #<2022
        # Intereses por depósitos de exigibilidad inmediata
        a=self.extraccion(610100000000)
        # Intereses por depósitos a plazo
        b=self.extraccion(610200000000)
        #c. Intereses por títulos de crédito emitidos
        c=self.extraccion(610300000000)
        # Intereses por préstamos interbancarios y de otros organismos
        d=self.extraccion(611400000000)
        # e. Intereses por obligaciones subordinadas
        e=self.extraccion(610600000000)
        # f. Intereses y rendimientos a cargo en operaciones de reporto y préstamo de valores
        f=self.extraccion(610400000000)
        # g. Premios a cargo
        g=self.extraccion(610700000000)
        # h. Descuentos y gastos de emisión por colocación de deuda
        h=self.extraccion(611100000000)
        # i. Costos y gastos asociados con el otorgamiento del crédito
        i=self.extraccion(611200000000)
        # j. Gastos provenientes de operaciones de cobertura
        j=self.extraccion(611900000000)
        # k. Pérdida por valorización
        k=self.extraccion(610800000000)
        #l. Intereses a cargo asociados con la cuenta global a que se refiere el artículo 61 de la Ley de Instituciones de Crédito
        l=self.extraccion(616100000000)
        # m. Incremento por actualización de gastos por intereses
        m=self.extraccion(619900000000)
        #n. Costo financiero por arrendamiento capitalizable
        n=self.extraccion(505024000000)
        n=abs(n)
        g_p_i=a+b+c+d+e+f+g+h+i+j+k+l+m+n 
        return g_p_i
    def activos_pro_22(self):
        #>2022
        # Efectivo y equivalentes de efectivo
        a=self.extraccion_ac(100200001001)#todo el periodo
        # Cartera de crédito con riesgo de crédito etapa 1
        b1=self.extraccion_ac(101800104001)#todo el periodo
        # Créditos otorgados en calidad de agente del gobierno federal (**)
        b3=self.extraccion_ac(101800105004)#todo el periodo
        # Cartera de crédito con riesgo de crédito etapa 2 
        b2=self.extraccion_ac(101800104002)#todo el periodo
        # Inversiones en instrumentos financieros
        c=self.extraccion_ac(100600001001)#todo el periodo
        # Préstamo de valores
        d=self.extraccion_ac(101200001001)#todo el periodo
        # Instrumentos financieros derivados
        e=self.extraccion_ac(101400001001)#todo el periodo ##p_a
        a_c=a+b1+b2-b3+c+d+e
        #
        #modelo_3
        if self.modelo==3:
            a_c=b1+b2-b3+c+d
        #
        #modelo_3_1
        if self.modelo==3.1:
            a_c=b1+b2-b3+c+d+e
        #modelo_3_2
        if self.modelo==3.2:
            a_c=a+b1+b2-b3+c+d
        return a_c
    def activos_pro_20(self):
        #<2022
        # a. Disponibilidades
        a=self.extraccion_ac(110000000000)
        # b. Cartera de crédito vigente
        b=self.extraccion_ac(130000000000)
        # c. Inversiones en valores
        c=self.extraccion_ac(120000000000)
        # d. Operaciones con valores y derivadas netas
        # Premios a recibir en operaciones de Préstamo de valores
        d1=self.extraccion_ac(120700000000)
        # Derivados
        d2=self.extraccion_ac(121400000000)
        # Préstamo de valores
        d3=self.extraccion_ac(220700000000)
        # Derivados
        d4=self.extraccion_ac(221400000000)
        d=d1+d2-d3-d4
        a_c=a+b+c+d 
        #modelo_3
        if self.modelo==3:
            d=d1-d3
            a_c=b+c+d
        # modelo_3_1
        if self.modelo==3.1:
            a_c=b+c+d
        #Modelo_3_2
        if self.modelo==3.2:
            d=d1-d3
            a_c=a+b+c+d
        return a_c
    def ingresos_dividendos_22(self):
        #>2022
        # Dividendos de inversiones permanentes
        a=self.extraccion(502201102139)
        # "Dividendos de instrumentos financieros que califican como instrumentos financieros de capital"  
        b=self.extraccion(500200102017)
        i_p_d=a+b    
        return i_p_d
    def ingresos_dividendos_20(self):
        #<2022
        # Dividendos de inversiones permanentes
        a=self.extraccion(505018000000)
        # b. Dividendos de instrumentos de patrimonio neto
        b=self.extraccion(511800000000)
        i_p_d=a+b
        return i_p_d
        ##
    def ingresos_operacion_22(self):
        # >2022
        # Recuperaciones
        a=self.extraccion(501600802086)
        # Ingresos por adquisición de cartera de crédito
        b=self.extraccion(501600802087)
        # Utilidad por venta de cartera de crédito
        c=self.extraccion(501600802089)
        # Ingreso por opción de compra en operaciones de arrendamiento financiero
        d=self.extraccion(501600802091)
        # Ingreso por participación del precio de venta de bienes en operaciones de arrendamiento financiero
        e=self.extraccion(501600802092)
        # Resultado en venta de bienes adjudicados
       
        f=self.extraccion(501600802098)
        if f<0:
            f=0
        # Resultado por valuación de bienes adjudicados
        g=self.extraccion(501600802099)
        if g<0:
            g=0
        # Resultado en venta de propiedades, mobiliario y equipo
        h=self.extraccion(501600802105)
        if h<0:
            h=0
        # Intereses a favor provenientes de préstamos a funcionarios y empleados
        i=self.extraccion(501600802107)
        # Resultado por valuación de los beneficios por recibir en operaciones de bursatilización
        j=self.extraccion(501600802109)
        if j<0:
            j=0
        # Resultado por valuación del activo por administración de activos financieros transferidos
        k=self.extraccion(501600802110)
        if k<0:
            k=0
        # Resultado por valuación del pasivo por administración de activos financieros transferidos
        l=self.extraccion(501600802111)
        if l<0:
            l=0
        # Resultado en beneficios por recibir en operaciones de bursatilización
        m=self.extraccion(501600802112)
        if m<0:
            m=0
        # Otras partidas de los ingresos (egresos) de la operación
        n=self.extraccion(501600802113)
        if n<0:
            n=0
        # Resultado por valorización de partidas no relacionadas con el margen financiero
        ñ=self.extraccion(501600802116)
        if ñ<0:
            ñ=0
        # Resultado por posición monetaria originado por partidas no relacionadas con el margen financiero (1)
        o=self.extraccion(501600802115)
        if o<0:
            o=0
        # Incremento por actualización de otros ingresos (egresos) de la operación (1)
        p=self.extraccion(501600802117)
        if p<0:
            p=0
        o_i_o=a+b+c+d+e+f+g+h+i+j+k+l+m+n+ñ+o+p
        return o_i_o
    def ingresos_operacion_20(self):
        # <2022
        # a. Recuperaciones de cartera de crédito
        a=self.extraccion(505040000000)
        # b. Recuperaciones
        b=self.extraccion(505023000000)
        # c. Ingresos por adquisición de cartera de crédito
        c=self.extraccion(505002000000)
        #d. Utilidad por cesión de cartera de crédito
        d=self.extraccion(505004000000)
        # e. Ingreso por opción de compra en operaciones de arrendamiento capitalizable
        e=self.extraccion(505012000000)
        # f. Ingreso por participación del precio de venta de bienes en operaciones de arrendamiento capitalizable
        f=self.extraccion(505013000000)
        # g. Resultado en venta de bienes adjudicados (siempre que sea positivo)
        g=self.extraccion(505015000000)
        if g<0:
            g=0
        #h. Resultado por valuación de bienes adjudicados (siempre que sea positivo)
        h=self.extraccion(505016000000)
        if h<0:
            h=0
        # i. Resultado en venta de propiedades, mobiliario y equipo (siempre que sea positivo)
        i=self.extraccion(505050000000)
        if i<0:
            i=0
        # j. Intereses a favor provenientes de préstamos a funcionarios y empleados
        j=self.extraccion(505031000000)
        # k. Resultado por valuación de los beneficios por recibir en operaciones de bursatilización (siempre que sea positivo)

        k=self.extraccion(505052000000)
        if k<0:
            k=0
        #l. Resultado por valuación del activo por administración de activos financieros transferidos (siempre que sea positivo)
        l=self.extraccion(505054000000)
        if l<0:
            l=0
        # m. Resultado por valuación del pasivo por administración de activos financieros transferidos (siempre que sea positivo)
        m=self.extraccion(505056000000)
        if m<0:
            m=0
        # n. Resultado en beneficios por recibir en operaciones de bursatilización (siempre que sea positivo)
        n=self.extraccion(505058000000)
        if n<0:
            n=0
        #ñ. Otras partidas de los ingresos (egresos) de la operación (siempre que sea positivo)
        ñ=self.extraccion(505090000000)
        if ñ<0:
            ñ=0
        # o. Utilidad por valorización de partidas no relacionadas con el margen financiero
        o=self.extraccion(505089000000)
        if o<0:
            o=0
        # p. Resultado por posición monetaria originado por partidas no relacionadas con el margen financiero (siempre que sea positivo)
        p=self.extraccion(505088000000)
        if p<0:
            p=0
        # q. Incremento por actualización de otros ingresos (egresos) de la operación (siempre que sea positivo)
        q=self.extraccion(505099000000)
        if q<0:
            q=0
        o_i_o=a+b+c+d+e+f+g+h+i+j+k+l+m+n+ñ+o+p+q
        return o_i_o
    def o_gasto_operacion_22(self):
        #>2022
        # Gastos por adquisición de cartera de crédito
        a=self.extraccion(501600802088)
        a=abs(a)
        # Pérdida por venta de cartera de crédito
        b=self.extraccion(501600802090)
        b=abs(b)
        # Quebrantos
        c=self.extraccion(501600802094)
        c=abs(c)
        # Donativos
        d=self.extraccion(501600802096)
        d=abs(d)
        # Resultado por adjudicación de bienes
        e=self.extraccion(501600802097)
        e=abs(e)
        # Resultado en venta de bienes adjudicados
      
        f=self.extraccion(501600802098)
        if f<0:
            f=abs(f)
        else:
            f=0
        # Resultado por valuación de bienes adjudicados
        g=self.extraccion(501600802099)
        if g<0:
            g=abs(g)
        else:
            g=0
        # Pérdida en custodia y administración de bienes
        h=self.extraccion(501600802101)
        h=abs(h)
        # Pérdida en operaciones de fideicomiso
        i=self.extraccion(501600802102)
        i=abs(i)
        # Intereses a cargo en financiamiento para adquisición de activos
        j=self.extraccion(501600802104)
        j=abs(j)
        # Resultado en venta de propiedades, mobiliario y equipo
        k=self.extraccion(501600802105)
        if k<0:
            k=abs(k)
        else:
            k=0
        # Resultado por valuación de los beneficios por recibir en operaciones de bursatilización
        l=self.extraccion(501600802109)
        if l<0:
            l=abs(l)
        else:
            l=0
        # Resultado por valuación del activo por administración de activos financieros transferidos
        m=self.extraccion(501600802110)
        if m<0:
            m=abs(m)
        else:
            m=0
        # Resultado por valuación del pasivo por administración de activos financieros transferidos
        n=self.extraccion(501600802111)
        if n<0:
            n=abs(n)
        else:
            n=0
        # Resultado en beneficios por recibir en operaciones de bursatilización
        ñ=self.extraccion(501600802112)
        if ñ<0:
            ñ=abs(ñ)
        else:
            ñ=0
        # Otras partidas de los ingresos (egresos) de la operación
        o=self.extraccion(501600802113)
        if o<0:
            o=abs(o)
        else:
            o=0
        # Incremento por actualización de otros ingresos (egresos) de la operación (1)
        p=self.extraccion(501600802117)
        if p<0:
            p=abs(p)
        else:
            p=0
        # Resultado por valorización de partidas no relacionadas con el margen financiero
        q=self.extraccion(501600802116)
        if q<0:
            q=abs(q)
        else:
            q=0
        #r=base_prueba.query("cve_concepto==501600802116").iloc[0][11]
        o_g_o=a+b+c+d+e+f+g+h+i+j+k+l+n+ñ+o+p+q
        return o_g_o
    def o_gasto_operacion_20(self):
        # <2022
        # a. Gastos por adquisición de cartera de crédito
        a=self.extraccion(505003000000)
        a=abs(a)
        # b. Pérdida por cesión de cartera de crédito
        b=self.extraccion(505005000000)
        b=abs(b)
        # c. Quebrantos
        c=self.extraccion(505026000000)
        c=abs(c)
        # Donativos
        d=self.extraccion(505007000000)
        d=abs(d)
        # e. Pérdida por adjudicación de bienes
        e=self.extraccion(505008000000)
        e=abs(e)
        # Resultado en venta de bienes adjudicados
        f=self.extraccion(505015000000)
        if f<0:
            f=abs(f)
        else:
            f=0
        # Resultado por valuación de bienes adjudicados
        g=self.extraccion(505016000000)
        if g<0:
            g=abs(g)
        else:
            g=0
        # Pérdida en custodia y administración de bienes
        h=self.extraccion(505010000000)
        h=abs(h)
        # Pérdida en operaciones de fideicomiso
        i=self.extraccion(505011000000)
        i=abs(i)
        # Intereses a cargo en financiamiento para adquisición de activos
        j=self.extraccion(505027000000)
        j=abs(j)
        # Resultado en venta de propiedades, mobiliario y equipo
        k=self.extraccion(505050000000)
        if k<0:
            k=abs(k)
        else:
            k=0
        # Resultado por valuación de los beneficios por recibir en operaciones de bursatilización
        l=self.extraccion(505052000000)
        if l<0:
            l=abs(l)
        else:
            l=0
        # Resultado por valuación del activo por administración de activos financieros transferidos
        m=self.extraccion(505054000000)
        if m<0:
            m=abs(m)
        else:
            m=0
        # Resultado por valuación del pasivo por administración de activos financieros transferidos
        n=self.extraccion(505056000000)
        if n<0:
            n=abs(n)
        else:
            n=0
        # Resultado en beneficios por recibir en operaciones de bursatilización
        ñ=self.extraccion(505058000000)
        if ñ<0:
            ñ=abs(ñ)
        else:
            ñ=0
        # Otras partidas de los ingresos (egresos) de la operación
        o=self.extraccion(505090000000)
        if o<0:
            o=abs(o)
        else:
            o=0
        # Incremento por actualización de otros ingresos (egresos) de la operación (1)
        p=self.extraccion(505099000000)
        if p<0:
            p=abs(p)
        else:
            p=0
        # q. Pérdida por valorización de partidas no relacionadas con el margen financiero
        q=self.extraccion(505089000000)
        if q<0:
            q=abs(q)
        else:
            q=0
        #r=base_prueba.query("cve_concepto==501600802116").iloc[0][11]
        o_g_o=a+b+c+d+e+f+g+h+i+j+k+l+n+ñ+o+p+q
        return o_g_o
    def comisiones_tarifas_22(self):
        # >2022
        # Avales
        a=self.extraccion(501000502047)
        # Cartas de crédito sin refinanciamiento
        b=self.extraccion(501000502048)
        # Aceptaciones por cuenta de terceros
        c=self.extraccion(501000502049)
        # Compraventa de instrumentos financieros
        d=self.extraccion(501000502050)
        # Apertura de cuenta
        e=self.extraccion(501000502051)
        # Manejo de cuenta
        f=self.extraccion(501000502052)
        # Actividades fiduciarias
        g=self.extraccion(501000502053)
        # Transferencia de fondos
        h=self.extraccion(501000502054)
        # Giros bancarios
        i=self.extraccion(501000502055)
        # Cheques de caja
        j=self.extraccion(501000502056)
        # Cheques certificados
        k=self.extraccion(501000502057)
        # Cheques de viajero
        l=self.extraccion(501000502058)
        # Custodia o administración de bienes
        m=self.extraccion(501000502059)
        # Alquiler de cajas de seguridad
        n=self.extraccion(501000502060)
        # Servicios de banca electrónica
        ñ=self.extraccion(501000502061)
        # Otras comisiones y tarifas cobradas
        o=self.extraccion(501000502062)
        # Operaciones de crédito
        p=self.extraccion(501000502045)
        c_t_c=a+b+c+d+e+f+g+h+i+j+k+l+m+n+ñ+o+p
        return c_t_c
    def comisiones_tarifas_20(self):
        # <2022
        # Avales
        a=self.extraccion(530100000000)
        # Cartas de crédito sin refinanciamiento
        b=self.extraccion(530200000000)
        # Aceptaciones por cuenta de terceros
        c=self.extraccion(530300000000)
        # Compraventa de valores
        d=self.extraccion(530400000000)
        # Apertura de cuenta
        e=self.extraccion(530500000000)
        # Manejo de cuenta
        f=self.extraccion(530600000000)
        # Actividades fiduciarias
        g=self.extraccion(530800000000)
        # Transferencia de fondos
        h=self.extraccion(530900000000)
        # Giros bancarios
        i=self.extraccion(531100000000)
        # Cheques de caja
        j=self.extraccion(531200000000)
        # Cheques certificados
        k=self.extraccion(531300000000)
        # Cheques de viajero
        l=self.extraccion(531400000000)
        # Custodia o administración de bienes
        m=self.extraccion(531500000000)
        # Alquiler de cajas de seguridad
        n=self.extraccion(531600000000)
        # Servicios de banca electrónica
        ñ=self.extraccion(531700000000)
        # Otras comisiones y tarifas cobradas
        o=self.extraccion(539000000000)
        # Operaciones de crédito
        p=self.extraccion(532100000000)
        c_t_c=a+b+c+d+e+f+g+h+i+j+k+l+m+n+ñ+o+p
        return c_t_c
    def comisiones_tarifas_p_22(self):
        #>2022
        # Bancos corresponsales
        a=self.extraccion(601200602064)
        # Comisionistas
        b=self.extraccion(601200602065)
        # Transferencia de fondos
        c=self.extraccion(601200602066)
        # Préstamos recibidos
        d=self.extraccion(601200602068)
        # Colocación de deuda
        e=self.extraccion(601200602069)
        # Otras comisiones y tarifas pagadas
        f=self.extraccion(601200602070)
        c_t_p=a+b+c+d+e+f
        return c_t_p
    def comisiones_tarifas_p_20(self):
        # <2022
        # Bancos corresponsales
        a=self.extraccion(630100000000)
        # Comisionistas
        b=self.extraccion(631200000000)
        # Transferencia de fondos
        c=self.extraccion(630200000000)
        # Préstamos recibidos
        d=self.extraccion(630400000000)
        # Colocación de deuda
        e=self.extraccion(631100000000)
        # Otras comisiones y tarifas pagadas
        f=self.extraccion(639000000000)
        c_t_p=a+b+c+d+e+f
        return c_t_p
    ##CF
    def resultado_compra_22(self):
        #>2022
        # Resultado por compraventa de instrumentos financieros e instrumentos financieros derivados
        a=self.extraccion(501400702077)
        # Resultado por compraventa de divisas
        b=self.extraccion(501400702079)
        # Resultado por compraventa de metales preciosos amonedados
        c=self.extraccion(501400702080)
        # Resultado por venta de colaterales recibidos
        d=self.extraccion(501400702081)
        #Costos de transacción
        e=self.extraccion(501400702082)
        r_c=a+b+c+d+e
        #primer modelo
        if self.modelo==1:
        # #resultado por valuacion de instrumentos financieros a valor razonable
            f=self.extraccion(501400702072)
        # # #resultado por valuacion de divisas
            g=self.extraccion(501400702074)
            r_c=a+b+c+d+e+f+g
        # # #
        # Modelo 1.1
        if self.modelo==1.1:
        # #resultado por valuacion de instrumentos financieros a valor razonable
            f=self.extraccion(501400702072)
            r_c=a+b+c+d+e+f
        if self.modelo==1.2:
            g=self.extraccion(501400702074)
            r_c=a+b+c+d+e+g
        # # #Modelo 2
        if self.modelo==2:
            f=self.extraccion(501400702072)
        # # #resultado por valuacion de divisas
            g=self.extraccion(501400702074)
            h=self.extraccion(501400702076)
            r_c=a+b+c+d+e+f+g+h
        return r_c
    def resultado_compra_20(self):
        # >2022
        # a. Valores e Instrumentos derivados
        a=self.extraccion(540300000000)
        # b. Divisas
        b=self.extraccion(540600000000)
        # c. Metales
        c=self.extraccion(540700000000)
        # d. Resultado por venta de colaterales recibidos
        d=self.extraccion(540900000000)
        # e. Costos de transacción
        e=self.extraccion(541000000000)
        r_c=a+b+c+d+e
        #modelo1
        if self.modelo==1:
        #resultado por valuacion de instrumentos financieros a valor razonable
            f=self.extraccion(540100000000)
        # # resultado por valuacion de divisas
            g=self.extraccion(540400000000)
            r_c=a+b+c+d+e+f+g
        # # #Modelo 2
        if self.modelo==2:
            f=self.extraccion(540100000000)
        # # resultado por valuacion de divisas
            g=self.extraccion(540400000000)
            h=self.extraccion(540500000000)
            r_c=a+b+c+d+e+f+g+h
        return r_c
    ##
    def graf(self):
        if self.peri<202201:
            self.ob_base(self.peri)
            resu_1=self.resultado_compra_20()
            self.ob_base(self.peri-1)
            resu_2=self.resultado_compra_20()
            resu=resu_1-resu_2
        else:
            self.ob_base(self.peri)
            resu_1=self.resultado_compra_22()
            self.ob_base(self.peri-1)
            resu_2=self.resultado_compra_22()
            resu=resu_1-resu_2
        return resu
    def calculo(self):
        self.periodos()
        #CIAD
        ##
        if self.peri_t!=12:
            self.ob_base(self.peri)
            i_p_i_1_0=self.ingresos_interes_22()/1000000
            #
            self.ob_base(self.peri_1)
            i_p_i_1_1=self.ingresos_interes_22()/1000000
            #
            self.ob_base(self.peri_1_1)
            i_p_i_2_0=self.ingresos_interes_22()/1000000
            #
            i_p_i_1_2=i_p_i_1_1-i_p_i_2_0
            i_p_i_1=i_p_i_1_0+i_p_i_1_2
            #
            self.ob_base(self.peri_2)
            i_p_i_2_1=self.ingresos_interes_20()/1000000
            #
            self.ob_base(self.peri_2_1)
            i_p_i_3_0=self.ingresos_interes_20()/1000000
            #
            i_p_i_2_2=i_p_i_2_1-i_p_i_3_0
            i_p_i_2=i_p_i_2_0+i_p_i_2_2
            #
            self.ob_base(self.peri_3)
            i_p_i_3_1=self.ingresos_interes_20()/1000000
            #
            self.ob_base(self.peri_3_1)
            i_p_i_4_0=self.ingresos_interes_20()/1000000
            #
            i_p_i_3_2=i_p_i_3_1-i_p_i_4_0
            i_p_i_3=i_p_i_3_0+i_p_i_3_2
            #
            self.ob_base(self.peri)
            g_p_i_1_0=self.gastos_intereses_22()/1000000
            #
            self.ob_base(self.peri_1)
            g_p_i_1_1=self.gastos_intereses_22()/1000000
            #
            self.ob_base(self.peri_1_1)
            g_p_i_2_0=self.gastos_intereses_22()/1000000
            g_p_i_1_2=g_p_i_1_1-g_p_i_2_0
            g_p_i_1=g_p_i_1_0+g_p_i_1_2
            #
            self.ob_base(self.peri_2)
            g_p_i_2_1=self.gastos_intereses_20()/1000000
            #
            self.ob_base(self.peri_2_1)
            g_p_i_3_0=self.gastos_intereses_20()/1000000
            g_p_i_2_2=g_p_i_2_1-g_p_i_3_0
            g_p_i_2=g_p_i_2_0+g_p_i_2_2
            #
            self.ob_base(self.peri_3)
            g_p_i_3_1=self.gastos_intereses_20()/1000000
            self.ob_base(self.peri_3_1)
            g_p_i_4_0=self.gastos_intereses_20()/1000000
            g_p_i_3_2=g_p_i_3_1-g_p_i_4_0
            g_p_i_3=g_p_i_3_0+g_p_i_3_2
            INA=abs(i_p_i_1-g_p_i_1)+abs(i_p_i_2-g_p_i_2)+abs(i_p_i_3-g_p_i_3)
            #
            self.ob_base_ac(self.peri)
            a_c_1=self.activos_pro_22()/1000000
            self.ob_base_ac(self.peri_1)
            a_c_2=self.activos_pro_22()/1000000
            self.ob_base_ac(self.peri_2)
            a_c_3=self.activos_pro_20()/1000000
            self.ob_base_ac(self.peri_3)
            a_c_4_1=self.activos_pro_20()/1000000
            self.ob_base_ac(self.peri_3_1-1)
            a_c_4_2=self.activos_pro_20()/1000000
            a_c_4=a_c_4_1-a_c_4_2
            #
            AC=(a_c_1+a_c_2+a_c_3+a_c_4)/36
            #
            self.ob_base(self.peri)
            i_p_d_1_0=self.ingresos_dividendos_22()/1000000
            self.ob_base(self.peri_1)
            i_p_d_1_1=self.ingresos_dividendos_22()/1000000
            self.ob_base(self.peri_1_1)
            i_p_d_2_0=self.ingresos_dividendos_22()/1000000
            i_p_d_1_2=i_p_d_1_1-i_p_d_2_0
            i_p_d_1=i_p_d_1_0+i_p_d_1_2
            #
            self.ob_base(self.peri_2)
            i_p_d_2_1=self.ingresos_dividendos_20()/1000000
            self.ob_base(self.peri_2_1)
            i_p_d_3_0=self.ingresos_dividendos_20()/1000000
            i_p_d_2_2=i_p_d_2_1-i_p_d_3_0
            i_p_d_2=i_p_d_2_0+i_p_d_2_2
            #
            self.ob_base(self.peri_3)
            i_p_d_3_1=self.ingresos_dividendos_20()/1000000
            self.ob_base(self.peri_3_1)
            i_p_d_4_0=self.ingresos_dividendos_20()/1000000
            i_p_d_3_2=i_p_d_3_1-i_p_d_4_0
            i_p_d_3=i_p_d_3_0+i_p_d_3_2
            #
            IDA=(i_p_d_1+i_p_d_2+i_p_d_3)/3
            #
            CIAD=min(1/3*INA,AC*0.0225)+IDA
        else:
            self.ob_base(self.peri)
            i_p_i_1=self.ingresos_interes_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212:
                i_p_i_2=self.ingresos_interes_20()/1000000
            else:
                i_p_i_2=self.ingresos_interes_22()/1000000
            #
            self.ob_base(self.peri_2)
            i_p_i_3=self.ingresos_interes_20()/1000000
            #
            ##
            self.ob_base(self.peri)
            g_p_i_1=self.gastos_intereses_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212:
                g_p_i_2=self.gastos_intereses_20()/1000000
            else:
                g_p_i_2=self.gastos_intereses_22()/1000000
            #
            self.ob_base(self.peri_2)
            g_p_i_3=self.gastos_intereses_20()/1000000
            #
            INA=abs(i_p_i_1-g_p_i_1)+abs(i_p_i_2-g_p_i_2)+abs(i_p_i_3-g_p_i_3)
            ##
            self.ob_base(self.peri)
            i_p_d_1=self.ingresos_dividendos_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212:
                i_p_d_2=self.ingresos_dividendos_20()/1000000
            else:
                i_p_d_2=self.ingresos_dividendos_22()/1000000
            
            #
            self.ob_base(self.peri_2)
            i_p_d_3=self.ingresos_dividendos_20()/1000000
            #
            IDA=(i_p_d_1+i_p_d_2+i_p_d_3)/3
            ##
            self.ob_base_ac(self.peri)
            a_c_1=self.activos_pro_22()/1000000
            self.ob_base_ac(self.peri_1)
            if self.peri==202212:
                a_c_2=self.activos_pro_20()/1000000
            else:
                a_c_2=self.activos_pro_22()/1000000
            self.ob_base_ac(self.peri_2)
            a_c_3=self.activos_pro_20()/1000000
            #
            AC=(a_c_1+a_c_2+a_c_3)/36
            ##
            CIAD=min(1/3*INA,AC*0.0225)+IDA
        ##CS
        if self.peri_t!=12:
            #
            self.ob_base(self.peri)
            o_i_o_1_0=self.ingresos_operacion_22()/1000000
            self.ob_base(self.peri_1)
            o_i_o_1_1=self.ingresos_operacion_22()/1000000
            self.ob_base(self.peri_1_1)
            o_i_o_2_0=self.ingresos_operacion_22()/1000000
            o_i_o_1_2=o_i_o_1_1-o_i_o_2_0
            o_i_o_1=o_i_o_1_0+o_i_o_1_2
            #
            self.ob_base(self.peri_2)
            o_i_o_2_1=self.ingresos_operacion_20()/1000000
            self.ob_base(self.peri_2_1)
            o_i_o_3_0=self.ingresos_operacion_20()/1000000
            o_i_o_2_2=o_i_o_2_1-o_i_o_3_0
            o_i_o_2=o_i_o_2_0+o_i_o_2_2
            #
            self.ob_base(self.peri_3)
            o_i_o_3_1=self.ingresos_operacion_20()/1000000
            self.ob_base(self.peri_3_1)
            o_i_o_4_0=self.ingresos_operacion_20()/1000000
            o_i_o_3_2=o_i_o_3_1-o_i_o_4_0
            o_i_o_3=o_i_o_3_0+o_i_o_3_2
            #
            OIOA=o_i_o_1+o_i_o_2+o_i_o_3
            #
            #
            self.ob_base(self.peri)
            o_g_o_1_0=self.o_gasto_operacion_22()/1000000
            self.ob_base(self.peri_1)
            o_g_o_1_1=self.o_gasto_operacion_22()/1000000
            self.ob_base(self.peri_1_1)
            o_g_o_2_0=self.ingresos_operacion_22()/1000000
            o_g_o_1_2=o_g_o_1_1-o_g_o_2_0
            o_g_o_1=o_g_o_1_0+o_g_o_1_2
            #
            self.ob_base(self.peri_2)
            o_g_o_2_1=self.o_gasto_operacion_20()/1000000
            self.ob_base(self.peri_2_1)
            o_g_o_3_0=self.o_gasto_operacion_20()/1000000
            o_g_o_2_2=o_g_o_2_1-o_g_o_3_0
            o_g_o_2=o_g_o_2_0+o_g_o_2_2
            #
            self.ob_base(self.peri_3)
            o_g_o_3_1=self.o_gasto_operacion_20()/1000000
            self.ob_base(self.peri_3_1)
            o_g_o_4_0=self.o_gasto_operacion_20()/1000000
            o_g_o_3_2=o_g_o_3_1-o_g_o_4_0
            o_g_o_3=o_g_o_3_0+o_g_o_3_2
            #
            OGOA=o_g_o_1+o_g_o_2+o_g_o_3
            ##
            #Aplica para año 2023, para años posteriores modificar los datos
            #BANCOMEXT
            if self.inst==37006:
               OGOA=OGOA-13910
            #BANOBRAS':37009
            if self.inst==37009:
               OGOA=OGOA-32400
            #'BANJERCITO':37019
            if self.inst==37019:
               OGOA=OGOA-2000
            #'NAFIN':37135
            if self.inst==37135:
               OGOA=OGOA-21237
            #'BANSEFI':37166
            if self.inst==37166:
               OGOA=OGOA-550
            #'SHF':37168
            if self.inst==37168:
               OGOA=OGOA-380
            #
            #
            self.ob_base(self.peri)
            c_t_c_1_0=self.comisiones_tarifas_22()/1000000
            self.ob_base(self.peri_1)
            c_t_c_1_1=self.comisiones_tarifas_22()/1000000
            self.ob_base(self.peri_1_1)
            c_t_c_2_0=self.comisiones_tarifas_22()/1000000
            c_t_c_1_2=c_t_c_1_1-c_t_c_2_0
            c_t_c_1=c_t_c_1_0+c_t_c_1_2
            #
            self.ob_base(self.peri_2)
            c_t_c_2_1=self.comisiones_tarifas_20()/1000000
            self.ob_base(self.peri_2_1)
            c_t_c_3_0=self.comisiones_tarifas_20()/1000000
            c_t_c_2_2=c_t_c_2_1-c_t_c_3_0
            c_t_c_2=c_t_c_2_0+c_t_c_2_2
            #
            self.ob_base(self.peri_3)
            c_t_c_3_1=self.comisiones_tarifas_20()/1000000
            self.ob_base(self.peri_3_1)
            c_t_c_4_0=self.comisiones_tarifas_20()/1000000
            c_t_c_3_2=c_t_c_3_1-c_t_c_4_0
            c_t_c_3=c_t_c_3_0+c_t_c_3_2
            #
            CTCA=c_t_c_1+c_t_c_2+c_t_c_3
        ##
            #
            self.ob_base(self.peri)
            c_t_p_1_0=self.comisiones_tarifas_p_22()/1000000
            self.ob_base(self.peri_1)
            c_t_p_1_1=self.comisiones_tarifas_p_22()/1000000
            self.ob_base(self.peri_1_1)
            c_t_p_2_0=self.comisiones_tarifas_p_22()/1000000
            c_t_p_1_2=c_t_p_1_1-c_t_p_2_0
            c_t_p_1=c_t_p_1_0+c_t_p_1_2
            #
            self.ob_base(self.peri_2)
            c_t_p_2_1=self.comisiones_tarifas_p_20()/1000000
            self.ob_base(self.peri_2_1)
            c_t_p_3_0=self.comisiones_tarifas_p_20()/1000000
            c_t_p_2_2=c_t_p_2_1-c_t_p_3_0
            c_t_p_2=c_t_p_2_0+c_t_p_2_2
            #
            self.ob_base(self.peri_3)
            c_t_p_3_1=self.comisiones_tarifas_p_20()/1000000
            self.ob_base(self.peri_3_1)
            c_t_p_4_0=self.comisiones_tarifas_p_20()/1000000
            c_t_p_3_2=c_t_p_3_1-c_t_p_4_0
            c_t_p_3=c_t_p_3_0+c_t_p_3_2
            #
            CTPA=c_t_p_1+c_t_p_2+c_t_p_3
            ##
            CS=max(1/3*OIOA,1/3*OGOA)+max(1/3*CTCA,1/3*CTPA) 
        else:
            #
            self.ob_base(self.peri)
            o_i_o_1=self.ingresos_operacion_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212: 
                o_i_o_2=self.ingresos_operacion_20()/1000000
            else:
                o_i_o_2=self.ingresos_operacion_22()/1000000
            #
            self.ob_base(self.peri_2)
            o_i_o_3=self.ingresos_operacion_20()/1000000
            #
            OIOA=o_i_o_1+o_i_o_2+o_i_o_3
            # print(OIOA)
            ##
            #
            self.ob_base(self.peri)
            o_g_o_1=self.o_gasto_operacion_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212: 
                o_g_o_2=self.o_gasto_operacion_20()/1000000
            else:
                o_g_o_2=self.o_gasto_operacion_22()/1000000
            #
            self.ob_base(self.peri_2)
            o_g_o_3=self.o_gasto_operacion_20()/1000000
            #
            OGOA=o_g_o_1+o_g_o_2+o_g_o_3
            ##
            self.ob_base(self.peri)
            c_t_c_1=self.comisiones_tarifas_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212: 
                c_t_c_2=self.comisiones_tarifas_20()/1000000
            else:
                c_t_c_2=self.comisiones_tarifas_22()/1000000
            #
            self.ob_base(self.peri_2)
            c_t_c_3=self.comisiones_tarifas_20()/1000000
            #
            CTCA=c_t_c_1+c_t_c_2+c_t_c_3
            ##
            self.ob_base(self.peri)
            c_t_p_1=self.comisiones_tarifas_p_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212: 
                c_t_p_2=self.comisiones_tarifas_p_20()/1000000
            else:
                c_t_p_2=self.comisiones_tarifas_p_22()/1000000
            #
            self.ob_base(self.peri_2)
            c_t_p_3=self.comisiones_tarifas_p_20()/1000000
            ##
            CTPA=c_t_p_1+c_t_p_2+c_t_p_3
            ##
            CS=max(1/3*OIOA,1/3*OGOA)+max(1/3*CTCA,1/3*CTPA)
        if self.peri_t!=12:
            self.ob_base(self.peri)
            r_c_1_0=self.resultado_compra_22()/1000000
            self.ob_base(self.peri_1)
            r_c_1_1=self.resultado_compra_22()/1000000
            self.ob_base(self.peri_1_1)
            r_c_2_0=self.resultado_compra_22()/1000000
            r_c_1_2=r_c_1_1-r_c_2_0
            r_c_1=r_c_1_0+r_c_1_2
            #
            self.ob_base(self.peri_2)
            r_c_2_1=self.resultado_compra_20()/1000000
            self.ob_base(self.peri_2_1)
            r_c_3_0=self.resultado_compra_20()/1000000
            r_c_2_2=r_c_2_1-r_c_3_0
            r_c_2=r_c_2_0+r_c_2_2
            #
            self.ob_base(self.peri_3)
            r_c_3_1=self.resultado_compra_20()/1000000
            self.ob_base(self.peri_3_1)
            r_c_4_0=self.resultado_compra_20()/1000000
            r_c_3_2=r_c_3_1-r_c_4_0
            r_c_3=r_c_3_0+r_c_3_2
            ##
            RCA=abs(r_c_3)+abs(r_c_2)+abs(r_c_1)
            ##
            CF=1/3*RCA
        else:
            self.ob_base(self.peri)
            r_c_1=self.resultado_compra_22()/1000000
            #
            self.ob_base(self.peri_1)
            if self.peri==202212: 
                r_c_2=self.resultado_compra_20()/1000000
            else:
                r_c_2=self.resultado_compra_22()/1000000
            #
            self.ob_base(self.peri_2)
            r_c_3=self.resultado_compra_20()/1000000
            RCA=abs(r_c_3)+abs(r_c_2)+abs(r_c_1)
            CF=1/3*RCA
        #print(CS)
        IN=CIAD+CS+CF
        return CIAD,CS,CF,IN
class calculo_RC:
    def __init__(self,periodo,institucion,años,monto,saldo,modelo):
        self.peri=periodo
        self.inst=institucion
        self.años=años
        self.monto=monto
        self.saldo=saldo
        self.modelo=modelo
    def riesgo(self):
        CIAD,CS,CF,IN=calculo_IN(self.peri,self.inst,self.saldo,self.modelo).calculo()
        #print(IN)
        UDI=7.86 #la del corte
        UDI_1=UDI*3500
        UDI_2=UDI*100500
        if IN<=UDI_1:
            CIN=IN*0.12
        if 3500*UDI<IN<=104000*UDI:
            CIN=(UDI_1*0.12)+((IN-UDI_1)*0.15)
        if IN>104000*UDI:
            CIN=(UDI_1*0.12)+(UDI_2*0.15)+((IN-(104000*UDI))*0.18)
        self.cin=CIN
        return  CIAD,CS,CF,IN,CIN
    def Calculo_MPI(self,cin,años):
        if años==10:
            peri_a=self.peri-1000
        if años==9:
            peri_a=self.peri-1000+1
        if años==8:
            peri_a=self.peri-1000+2
        if años==7:
            peri_a=self.peri-1000+3 
        base_p=base_pi.query("cve_institucion==@self.inst and cve_periodo<=@self.peri and cve_periodo>=@peri_a")
        base_p_a=base_pi_a.query("cve_institucion==@self.inst and cve_periodo<=@self.peri and cve_periodo>=@peri_a")
        base_p_a=base_p_a.sort_values("dat_ult_fech_modif_o_reg_evto",ascending=False,ignore_index=True)
        lista=list(base_p_a["dat_num_evto_sencillo"])
        base_p_a["monto_total"]=base_p_a["dat_monto_perdida_actualizado"]+base_p_a["dat_monto_gasto"]-base_p_a["dat_monto_recuperacion"]
        base_p["monto_total"]=base_p["dat_monto_perdida"]+base_p["dat_monto_gasto"]-base_p["dat_monto_recuperacion"]
        base_p_a_d=base_p_a.loc[:,"dat_num_evto_sencillo"].drop_duplicates()
        lista_d=base_p_a_d.index.tolist()
        base_p_a=base_p_a.loc[lista_d,:]
        base_p_a=base_p_a.query("monto_total>=@self.monto")
        suma=sum(base_p_a["monto_total"])
        # print("si")
        base_p=base_p[~base_p["dat_num_evto_sencillo"].isin(lista)]
        base_p=base_p.loc[:,["dat_num_evto_sencillo","monto_total"]]
        base_p=base_p.query("monto_total>=@self.monto")
        base_p=base_p.drop_duplicates()
        suma=suma+sum(base_p["monto_total"])
        # print("si_2")
        suma=suma/1000000
        PI=(suma/self.años)*15
        #print(self.años)
        try:
            MPI=max((np.log(np.exp(1)-1+pow(PI/cin,0.8))),1)
        except:
            MPI=0
        banc_m=[40152,40062,40042,40143,40139.40145]
        if self.inst in banc_m:
            MPI=(np.log(np.exp(1)-1+pow(PI/cin,0.8)))
            print("si")
            print(MPI)
        if self.inst==40139:
            MPI=(np.log(np.exp(1)-1+pow(PI/cin,0.8)))
            print("si")
            print(MPI)
        return MPI
    def calculo(self):
        CIAD,CS,CF,in_c,cin_c=self.riesgo()
        MPI=self.Calculo_MPI(cin_c,self.años)
        try:
            RC=round(MPI*self.cin)
        except:
            RC=0
        return in_c,cin_c,MPI,RC
bancos_BM={'BANCOMEXT':37006,'BANOBRAS':37009,'BANJERCITO':37019,'NAFIN':37135,'BANSEFI':37166,'SHF':37168,'ABC Capital': 40138,'Accendo Banco': 40102,'Actinver': 40133,'Afirme': 40062,'American Express': 40103,'Autofin': 40128,'Banamex': 40002,'Banamex Consolidado': 102,'Banca Mifel': 40042,
 'Bancen': 40086,'Banco Ahorro Famsa': 40131,'Banco Azteca': 40127,'Banco Base': 40145,'Banco Bicentenario': 40146,'Banco del Bajío': 40030,'Banco Deuno': 40142,'Banco S3': 40160,'Banco Wal-Mart': 40134,
 'BanCoppel': 40137,'Bancrea': 40152,'Bank of America': 40106,'Bank of China': 40159,'Bankaool': 40147,'Banorte': 40072,'Banregio': 40058,'Bansí': 40060,'Barclays': 40129,'BBVA Bancomer Servicios': 40017,
 'BBVA México': 40012,'BIAfirme': 40139,'BNP Paribas México': 40164,'CIBanco': 40143,'Compartamos': 40130,'Consubanco': 40140,'Covalto': 40154,'Credit Suisse': 40126,'Deutsche Bank': 40124,
 'Dondé Banco': 40151,'Forjadores': 40149,'Ge Money': 40022,'HSBC': 40021,'ICBC': 40155,'Inbursa': 40036,'ING': 40116,'Inmobiliario Mexicano': 40150,'Interacciones': 40037,'Intercam Banco': 40136,
 'Invex': 40059,'Ixe': 40032,'Ixe Consolidado': 132,'J.P. Morgan': 40110,'KEB Hana México': 40162,'Mizuho Bank': 40158,'Monex': 40112,'MUFG Bank': 40108,'Multiva': 40132,'Pagatodo': 40148,'Sabadell': 40156,
 'Santander': 40014,'Santander Consolidado': 114,'Scotiabank': 40044,'Shinhan': 40157,'The Bank Of New York Mellon': 40144,'Ve por Más': 40113,'Volkswagen Bank': 40141,
 'Banca de Inversión y Otros Servicios': 61,'Banca de Inversión y Otros Servicios Consolidado': 67,'Bancos Cambiarios': 60,'Bancos Cambiarios Consolidado': 66,'Comercial Mediano': 62,
 'Comercial Mediano Consolidado': 68,'Comercial Pequeño': 63,'Comercial Pequeño Consolidado': 69,'Créditos a los Hogares': 64,'Créditos a los Hogares Consolidado': 70}

bank=["BANCOMEXT","BANOBRAS","BANJERCITO","NAFIN","BANSEFI","SHF","ABC Capital",
"Actinver",
"Afirme",
"American Express",
"Autofin",
"Banamex",
"Banca Mifel",
"Banco Azteca",
"Banco Base",
"Banco del Bajío",
"Banco S3",
"BanCoppel",
"Bancrea",
"Bank of America",
"Bank of China",
"Bankaool",
"Banorte",
"Banregio",
"Bansí",
"Barclays",
"BBVA México",
"BIAfirme",
"BNP Paribas México",
"CIBanco",
"Compartamos",
"Consubanco",
"Covalto",
"Credit Suisse",
"Deutsche Bank",
"Dondé Banco",
"Forjadores",
"HSBC",
"ICBC",
"Inbursa",
"Inmobiliario Mexicano",
"Intercam Banco",
"Invex",
"J.P. Morgan",
"KEB Hana México",
"Mizuho Bank",
"Monex",
"MUFG Bank",
"Multiva",
"Pagatodo",
"Sabadell",
"Santander",
"Scotiabank",
"Shinhan",
"Ve por Más",
"Volkswagen Bank"]
#Actual
a_p=[10,9,8]
resultados=[]
periodo=202309
monto=0
#Calculo del RC de todos los bancos y con los años 8,9 y 10
if periodo<202212:
    print("ingresa un periodo mayor a 202212")
else:
    for i in bank:
        sal=130
        if i=="Banamex" or i=="BANSEFI":
            sal=132
        if i=="Invex":
            sal=136
        for j in a_p:
            if j==10:
                in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],j,monto,sal,0).calculo()
                re_r=[i,bancos_BM[i],in_i,cin_i,mpi_i,rc_i]
                #print(bancos_BM[i],in_i,cin_i)
            else: 
                MPI=calculo_RC(periodo, bancos_BM[i],j,monto,sal,0).Calculo_MPI(cin_i,j)
                RC=round(MPI*cin_i)
                re_r.append(MPI)
                re_r.append(RC)
        resultados.append(re_r)
        print(sal)
    resultados=pd.DataFrame(resultados)
    resultados.columns=["Banco","ID","IN","CIN","MPI_10","RC_10","MPI_9","RC_9","MPI_8","RC_8"]
# resultados.to_csv("D:\\IDSS3399\\OneDrive - Comision Nacional Bancaria y de Valores\\Escritorio\\python\\resultado riesgo 202309_M3_1.csv")
#------------------------------------------------------------------------------
#Calculo del RC para los modelos y calibrado para 202309

bank=["ABC Capital",
"Actinver",
"Afirme",
"Autofin",
"Banca Mifel",
"Banco Base",
"Banco S3",
"BanCoppel",
"Bancrea",
"BANJERCITO",
"Bank of America",
"Bank of China",
"Bankaool",
"BANOBRAS",
"Bansí",
"BBVA México",
"BIAfirme",
"BNP Paribas México",
"CIBanco",
"Consubanco",
"Covalto",
"Credit Suisse",
"Deutsche Bank",
"Dondé Banco",
"ICBC",
"Inbursa",
"Intercam Banco",
"Invex",
"J.P. Morgan",
"KEB Hana México",
"Mizuho Bank",
"Monex",
"MUFG Bank",
"Multiva",
"NAFIN",
"Pagatodo",
"Sabadell",
"Santander",
"SHF",
"Shinhan",
"Ve por Más"
]
resultados=[]
periodo=202309
monto=0
if periodo<202212:
    print("ingresa un periodo mayor a 202212")
else:
    for i in bank:
        sal=130
        if i=="Banamex" or i=="BANSEFI":
            sal=132
        if i=="Invex":
            sal=136
        in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],8,monto,sal,0).calculo()
        in_i_1,cin_i_1,mpi_i_1,rc_i_1=calculo_RC(periodo, bancos_BM[i],8,monto,sal,1).calculo()
        in_i_2,cin_i_2,mpi_i_2,rc_i_2=calculo_RC(periodo, bancos_BM[i],8,monto,sal,2).calculo()
        in_i_3,cin_i_3,mpi_i_3,rc_i_3=calculo_RC(periodo, bancos_BM[i],8,monto,sal,3).calculo()
        re_r=[i,bancos_BM[i],rc_i,rc_i_1,rc_i_2,rc_i_3]
        resultados.append(re_r)
    resultados=pd.DataFrame(resultados)
    resultados.columns=["Banco","ID","RC","RC_1","RC_2","RC_3"]

#10
bank=[
"Banco Azteca",
"Banco del Bajío",
"BANCOMEXT",
"Banorte",
"Barclays",
"Compartamos",
"Forjadores",
"HSBC",
"Inmobiliario Mexicano",
"Scotiabank"
      ]
resultados_2=[]
periodo=202309
monto=0
if periodo<202212:
    print("ingresa un periodo mayor a 202212")
else:
    for i in bank:
        sal=130
        if i=="Banamex" or i=="BANSEFI":
            sal=132
        if i=="Invex":
            sal=136
        in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],10,monto,sal,0).calculo()
        in_i_1,cin_i_1,mpi_i_1,rc_i_1=calculo_RC(periodo, bancos_BM[i],10,monto,sal,1).calculo()
        in_i_2,cin_i_2,mpi_i_2,rc_i_2=calculo_RC(periodo, bancos_BM[i],10,monto,sal,2).calculo()
        in_i_3,cin_i_3,mpi_i_3,rc_i_3=calculo_RC(periodo, bancos_BM[i],10,monto,sal,3).calculo()
        re_r=[i,bancos_BM[i],rc_i,rc_i_1,rc_i_2,rc_i_3]
        resultados_2.append(re_r)
    resultados_2=pd.DataFrame(resultados_2)
    resultados_2.columns=["Banco","ID","RC","RC_1","RC_2","RC_3"]
# 9
bank=["Banregio",
        "Volkswagen Bank",
        "Banamex",
        "BANSEFI"]
resultados_3=[]
periodo=202309
monto=0
if periodo<202212:
    print("ingresa un periodo mayor a 202212")
else:
    for i in bank:
        sal=130
        if i=="Banamex" or i=="BANSEFI":
            sal=132
        if i=="Invex":
            sal=136
        in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],10,monto,sal,0).calculo()
        in_i_1,cin_i_1,mpi_i_1,rc_i_1=calculo_RC(periodo, bancos_BM[i],10,monto,sal,1).calculo()
        in_i_2,cin_i_2,mpi_i_2,rc_i_2=calculo_RC(periodo, bancos_BM[i],10,monto,sal,2).calculo()
        in_i_3,cin_i_3,mpi_i_3,rc_i_3=calculo_RC(periodo, bancos_BM[i],10,monto,sal,3).calculo()
        re_r=[i,bancos_BM[i],rc_i,rc_i_1,rc_i_2,rc_i_3]
        resultados_3.append(re_r)
     
    resultados_3=pd.DataFrame(resultados_3)
    resultados_3.columns=["Banco","ID","RC","RC_1","RC_2","RC_3"]
resultado_TM=pd.concat([resultados,resultados_2,resultados_3])
# resultado_TM.to_csv("D:\\IDSS3399\\OneDrive - Comision Nacional Bancaria y de Valores\\Escritorio\\python\\resultado riesgo 202309_M3_1.csv")
#------------------------------------------------------------------------------

# #revisando que pasa con banamex
# bank=["Banamex"]
# resultados_3=[]
# periodo=202309
# monto=0
# if periodo<202212:
#     print("ingresa un periodo mayor a 202212")
# else:
#     for i in bank:
#             sal=130
#             if i=="Banamex" or i=="BANSEFI":
#                 sal=132
#             if i=="Invex":
#                 sal=136
#             in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],9,monto,sal,0).calculo()
#             re_r=[i,bancos_BM[i],periodo,in_i,cin_i,mpi_i,rc_i]
#             in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],9,monto,sal,1).calculo()
#             re_r.append(rc_i)
#             in_i,cin_i,mpi_i,rc_i=calculo_RC(periodo, bancos_BM[i],9,monto,sal,2).calculo()
#             re_r.append(rc_i)
#             resultados_3.append(re_r)
     
#     resultados_3=pd.DataFrame(resultados_3)
#     resultados_3.columns=["Banco","ID","Periodo","IN","CIN","MPI","RC","RC_M1","RC_M2"] 

