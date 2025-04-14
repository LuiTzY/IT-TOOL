from django.db import models



class OS(models.Model):
    
    OS_TYPES = [
        ('Linux','Linux'),
        ('Windows','Windows')
        ]
    
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    os_img =  models.ImageField(upload_to="os", blank=True,null=True)
    os_type = models.CharField(max_length=30,choices=OS_TYPES, blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.nombre} - {self.version}"

class Server(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('mantenimiento', 'Mantenimiento'),
        ('sin uso', 'Retirado'),
    ]

    ENVIRONMENTS = [
        ('PROD', 'Produccion'),
        ('DEV', 'Desarrollo'),
        ('TEST', 'Pruebas'),
    ]
    SERVERS_TYPE = [
        ('WEB', 'Servidor Web'),
        ('DB', 'Servidor de Base de Datos'),
        ('APP', 'Servidor de Aplicaciones'),
        ('DNS', 'Servidor DNS'),
        ('FTP', 'Servidor FTP'),
        ('SMTP', 'Servidor de Correo'),
        ('FILES', 'Servidor de Archivos'),
        ('PROXY', 'Servidor Proxy'),
        ('OTHER', 'Otro'),
        ]

    #Nombre que le daremos al server, no es el que tiene como hostname si no uno que prefiramos darle
    server_name = models.CharField(max_length=100)
    #Ip del servidor, indicamos IPv4 ya que no utilizaremos otro protocolo
    ip = models.GenericIPAddressField(protocol='IPV4')
    #Hostname del servidor
    server_hostname = models.CharField(max_length=100)
    #Sistema operativo del servidor
    server_os = models.ForeignKey(OS, on_delete=models.SET_NULL, null=True)
    server_environment = models.CharField(max_length=10, choices=ENVIRONMENTS)
    server_status = models.CharField(max_length=20, choices=ESTADOS)
    server_type =  models.CharField(max_length=50,choices=SERVERS_TYPE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.server_name} ({self.ip})"
