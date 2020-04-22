from django.db import models
from django.urls import reverse

# VARIABLES NECESARIAS POR USAR
tipoGenero_Select= [('Masculino','Masculino'),('Femenino','Femenino')]


# MEDELOS -ORM
class Cita(models.Model):
    id_cita = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre_paciente = models.CharField(max_length=50, null=False, blank=False)
    motivo_consulta = models.CharField(max_length=100, null=False, blank=False)
    tipo_consulta = models.CharField(max_length=50, null=False, blank=False)
    telefono_contacto = models.CharField(max_length=15, null=False, blank=False)
    fecha = models.DateField()
    hora = models.TimeField()
    id_paciente = models.ForeignKey('Paciente', db_column='id_paciente', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_paciente
    
    def get_absolute_url(self):
        return reverse('cita-edit', kwargs={'pk':self.pk})
        
    class Meta:
        db_table = 'Cita'
        verbose_name_plural = 'Citas'


class Consulta(models.Model):
    id_consulta = models.CharField(primary_key=True, max_length=8, null=False, blank=False)
    diagnostico = models.CharField(max_length=100, null=False, blank=False)
    id_expediente = models.ForeignKey('Expediente', models.DO_NOTHING, db_column='id_expediente', null=False, blank=False)
    id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='id_empleado', null=False, blank=False)
    def __str__(self):
        return self.diagnostico
    
    def get_absolute_url(self):
        return reverse('consulta-edit', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Consulta'
        verbose_name_plural = 'Consultas'


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True, null=False, blank=False)
    nombres_empleado = models.CharField(max_length=50, null=False, blank=False)
    apellidos_empleado = models.CharField(max_length=50, null=False, blank=False)
    correo_electronico = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    tipo_usuario = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=10, null=False, blank=False)
    user = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombres_empleado
    
    def get_absolute_url(self):
        return reverse('empleado-edit', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Empleado'
        verbose_name_plural = 'Empleados'


class Expediente(models.Model):
    id_expediente = models.IntegerField(primary_key=True, null=False, blank=False)
    peso = models.FloatField(null=False, blank=False)
    pulso = models.IntegerField(null=False, blank=False)
    temperatura = models.FloatField(null=False, blank=False)
    presion_arterial = models.CharField(max_length=3, null=False, blank=False)
    nombre_refiere = models.CharField(max_length=50, null=False, blank=False)
    enfermedades_preexistentes = models.CharField(max_length=100, null=False, blank=False)
    alergias = models.CharField(max_length=50, null=False, blank=False)
    medicamentos_actuales = models.CharField(max_length=50, null=False, blank=False)
    observaciones = models.CharField(max_length=50, null=False, blank=False)
    id_cita = models.ForeignKey(Cita, db_column='id_cita', on_delete=models.CASCADE, null=False, blank=False)
    id_paciente = models.ForeignKey('Paciente', db_column='id_paciente', on_delete=models.CASCADE, null=False, blank=False)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', null=False, blank=False)
   
    def __str__(self):
        return self.id_expediente
    
    def get_absolute_url(self):
        return reverse('expediente-edit', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Expediente'
        verbose_name_plural = 'Expedientes'


class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True, null=False, blank=False)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=50, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    genero = models.CharField(max_length=20, choices=tipoGenero_Select, null=False, blank=False)
    telefono = models.CharField(max_length=15, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    correo_electronico = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombres
    
    def get_absolute_url(self):
        return reverse('paciente-edit', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Radiografia(models.Model):
    id_radiografia = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre_radiografia = models.CharField(max_length=50, null=False, blank=False)
    imagen_radiografia = models.CharField(max_length=50, null=False, blank=False)
    id_expediente = models.ForeignKey(Expediente, db_column='id_expediente', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nombre_radiografia
    
    def get_absolute_url(self):
        return reverse('radigrafia-detail', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Radiografia'
        verbose_name_plural = 'Radiografias'


class Receta(models.Model):
    id_receta = models.IntegerField(primary_key=True, null=False, blank=False)
    medicamento = models.CharField(max_length=50, null=False, blank=False)
    observaciones = models.CharField(max_length=100, null=False, blank=False)
    id_paciente = models.ForeignKey(Paciente, db_column='id_paciente', on_delete=models.CASCADE, null=False, blank=False)
    id_consulta = models.ForeignKey(Consulta,  db_column='id_consulta', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.medicamento
    
    def get_absolute_url(self):
        return reverse('receta-edit', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'Receta'
        verbose_name_plural = 'Recetas'