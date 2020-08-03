from django.db import models

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

#Importa los metodos
#from Tarea2.models import Producto,Cliente,Factura,DetalleFactura

#ingreso de productos

#forma1
#P = Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)
#P.save()
#Producto.objects.all()

#forma 2
#Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)

#Ingreso Cliente
#Primero se ingresa el Cliente y luego se agrega el Producto
#forma1
#C = Cliente(ruc='0989389387001',nombre='Maria',direccion='Av. Naranjito')
#C.save()
#C.producto.add(1)

#forma2
#Cliente.objects.create(ruc='0896778983001',nombre='Fernanda',direccion='Rocafuerte y 10 de mayo')
#Cliente.objects.all()[1].producto.add(2)

#Ingreso de Factura
#Para ingresar al cliente estamos reutilizando la variable C donde tenemos los datos del cliente, no es necesario identificar el id porque python detecta
#que variable es la que necesita mandar por el parametro

#forma 1
#F = Factura(cliente=C,fecha='2020-07-20',total=25)
#F.save()
#forma 2
#Factura.objects.create(cliente=Cliente.objects.get(id=5),fecha='2020-07-25',total=55.80)

#Ingreso de detallefactura

#forma 1
#Dt = DetalleFactura(factura=F,producto=P,cantidad=2,precio=10,subtotal=20)
#Dt.save()

#forma2
#DetalleFactura.objects.create(factura=F,producto=Producto.objects.get(id=2),cantidad=2,precio=2.5,subtotal=5)

#Modificar Producto
#Forma 1
#p = Producto.objects.get(id=1)
#p.precio = 1.13
#p.save()

#Forma2
#Producto.objects.filter(id=1).update(precio=1.7)

#Modificar Cliente
#Forma1
#c = Cliente.objects.get(id=4)
#c.direccion='Marta Roldos'
#c.save()

#Forma 2
#Cliente.objects.filter(id=5).update(direccion='Margaritas2')

#Forma Factura

#forma 1
#f = Factura.objects.get(id=1)
#f.fecha='2020-02-20'
#f.save()

#forma2
#Factura.objects.filter(id=2).update(fecha='2020-06-05')

# detalle factura
# forma 1
#dt = DetalleFactura.objects.get(id=1)
#dt.cantidad=4
#dt.save()

#forma 2
#DetalleFactura.objects.filter(id=2).update(cantidad=5)

#Eliminar
#Producto
#forma 1
#p = Producto.objects.get(id=2)
#p.delete()

#Forma 2
#Producto.objects.filter(id=1).delete()

#Cliente
#Forma 1
#c = Cliente.objects.get(id=4)
#c.delete()

#forma2
#Cliente.objects.filter(id=5).delete()

#Factura
# forma 1
#f = Factura.objects.get(id=3)
#f.delete()
# forma 2
#Factura.objects.filter(id=4).delete()


#detalleFactura
#forma 1
#dt = DetalleFactura.objects.get(id=3)
#dt.delete()

#forma2
#DetalleFactura.objects.filter(id=4).delete()

#Query de un modelo
#Producto.objects.all()
#Producto.objects.filter(id__lte=3)
#Producto.objects.exclude(descripcion__icontains='Cola')
#Producto.objects.filter(id__gte=7)
#Producto.objects.filter(id__gt=4).values('id','descripcion')
#Producto.objects.filter(id__lt=7).values('id','descripcion')
#Producto.objects.filter(descripcion='Coca Cola').values('id','descripcion')
#Factura.objects.filter(cliente__nombre='Maria')
#c= Cliente.objects.get(nombre='Maria')
#c.factura_set.all()
#c.factura_set.filter(id=5)
#Factura.objects.select_related('cliente').filter(cliente__nombre='Maria')
#Cliente.objects.prefetch_related('producto').filter(nombre='Maria').values('nombre','producto__descripcion')