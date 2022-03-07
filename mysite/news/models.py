from django.db import models

# Create your models here.


class News(models.Model):
    # создание БД
    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")  # blank=True - не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")   # записывает дату в момент создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано?")
    category = models.ForeignKey("category", on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        """Описание модели"""
        # наименование модели в админке в единственном числе
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        # порядок сортировки по ключу из БД
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наименование категорий")
    def __str__(self):
        return self.title
    class Meta:
        """Описание модели"""
        # наименование модели в админке в единственном числе
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        # порядок сортировки по ключу из БД
        ordering = ['title']