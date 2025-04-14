from django.db import models
from src.servers.models import Server

class DNS(models.Model):
    """
        Modelo representativo para los servidores dns que existan dentro de la empresa
    """
    name =  models.CharField(max_length=250)
    ip = models.GenericIPAddressField(protocol='IPV4')
    tipo = models.CharField(
        max_length=50,
        choices=[('interno', 'Interno'), ('externo', 'Externo'), ('cloud', 'Cloud')],
        default='interno'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.ip}"
        
class DNSEntry(models.Model):
    """
        Modelo representativo de las entradas DNS relacionadas a cada servidor
    """
    ENTRYS_TYPE = [
        ('A', 'A - Dirección IPv4'),
        ('AAAA', 'AAAA - Dirección IPv6'),
        ('PTR', 'PTR - Reversa'),
        ('CNAME', 'CNAME - Alias'),
        ('MX', 'MX - Mail Exchange'),
        ('TXT', 'TXT - Texto'),
        ('NS', 'NS - Nameserver'),
    ]
    entry_name = models.CharField(max_length=255)
    entry_type = models.CharField(max_length=10, choices=ENTRYS_TYPE)
    
    #Valor que tendra dependiendo del tipo de entrada que sea, si es A pues la ip y asi
    value = models.CharField(max_length=255)
    
    #Servidor al que va a estar relacionada esta entrada DNS
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True, related_name='entradas_dns')
    dns_server = models.ForeignKey(DNS, on_delete=models.SET_NULL, null=True, blank=True, related_name='entradas')
    
    created_at = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)
