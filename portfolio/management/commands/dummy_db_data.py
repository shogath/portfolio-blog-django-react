from datetime import datetime, timedelta

from django.core.management.commands.migrate import Command

from portfolio.models import PortfolioProject
from blog.models import Post


class Command(Command):
    """
    Add dummy data to database.
    """

    def handle(self, *args, **options):
        self.stdout.write('Creating dummy data...')

        for i in range(1, 100):
            post = Post()
            post.title = f'Post {i}'
            post.slug = f'post-{i}'
            post.image = 'coding_cropped.jpg'
            post.thumbnail = 'coding_thumbnail.jpg'
            post.excerpt = '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eu dui eget orci maximus placerat eu vitae leo. Sed nulla felis, convallis ut nibh at, mollis cursus erat. Cras quis enim gravida, feugiat eros vel, tempor quam.&nbsp;</p>'
            post.content = '''<p><strong>Lorem ipsum dolor sit amet</strong>, consectetur adipiscing elit. Nulla eu dui eget orci maximus placerat eu vitae leo. Sed nulla felis, convallis ut nibh at, mollis cursus erat. Cras quis enim gravida, feugiat eros vel, tempor quam. Morbi at ex egestas, sollicitudin mi ut, feugiat urna. Quisque arcu nisl, tempus vitae lobortis vel, varius eu lacus. Morbi rhoncus risus mollis est lobortis, id accumsan nulla blandit. Pellentesque neque orci, pulvinar at vehicula a, scelerisque nec orci. Proin ut ipsum in orci lacinia consequat ac et turpis. Nullam sodales fermentum pretium. In maximus nunc lacus, faucibus rhoncus turpis lobortis a. Sed sed mollis lectus. Nullam at nisi finibus, finibus nisi in, eleifend leo. Nunc sagittis ex placerat est ornare dictum vel non odio. Integer eget nibh a felis ullamcorper facilisis eget sit amet neque. Nulla viverra nisi at ex venenatis, ut euismod augue facilisis. Pellentesque elit dui, luctus et pretium at, elementum nec sapien.</p>

<p><img alt="" src="/files/django.png" style="height:137px; width:300px" /></p>

<p>Nulla ac nisi fermentum, posuere magna tincidunt, sollicitudin tellus. Quisque faucibus sagittis felis, vitae congue leo euismod eget. Vestibulum semper egestas sollicitudin. Vestibulum et neque ut diam efficitur mattis a non lectus. Duis vitae nunc molestie sapien semper iaculis. Aenean rutrum sagittis ligula, a dignissim enim pharetra id. In ac ligula dui.</p>

<p>In sem metus, gravida eget orci eget, lacinia pulvinar dui. Donec vitae arcu gravida, pulvinar sapien non, convallis justo. Mauris vitae facilisis dui. Praesent auctor sed orci ac aliquam. Sed interdum massa sit amet orci tincidunt, non lobortis magna luctus. Suspendisse pellentesque accumsan felis sit amet sollicitudin. Sed eu lobortis nisi. Nulla non risus in quam ornare finibus. Morbi ante magna, lobortis sed odio non, gravida rutrum felis. Aenean feugiat bibendum porttitor. Integer vehicula convallis ultrices. Proin sit amet dui arcu. Sed eleifend dolor quis finibus imperdiet. Mauris maximus, sem a sollicitudin vulputate, quam odio condimentum magna, at vulputate ante tellus vel quam. Pellentesque a tortor vel risus condimentum gravida id vel neque.</p>

<p>Suspendisse potenti. Donec vel justo leo. Sed venenatis, libero sit amet iaculis dapibus, quam magna faucibus leo, sit amet sodales enim ipsum vel velit. Ut rutrum tincidunt nisi sed blandit. Nullam imperdiet nisi mauris, sit amet interdum ex finibus et. Nullam scelerisque venenatis enim a interdum. Etiam pellentesque rutrum ullamcorper. Vestibulum sed neque nec sem aliquam consequat. Ut luctus molestie volutpat. Cras imperdiet erat eget arcu malesuada, non pellentesque est sollicitudin. Aliquam enim erat, varius in gravida non, fringilla eu ex. Etiam facilisis, ligula non rutrum egestas, libero lectus cursus turpis, ut ullamcorper tellus purus eu sem. Proin placerat sem non justo placerat convallis. Donec eleifend quam lacus, at dictum lorem bibendum id. In ut ante urna.</p>

<p>Etiam ac sapien et quam pretium auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget malesuada mi. Nam convallis est eget aliquam lobortis. Mauris tristique congue mattis. Aliquam at eleifend neque, aliquam laoreet sapien. Quisque velit mauris, volutpat at odio ac, varius faucibus dolor. In eget odio eget leo pulvinar consequat a in leo. Ut sapien metus, pellentesque laoreet lacinia in, porttitor sed turpis. Fusce bibendum lacinia interdum. Sed a nunc in risus condimentum ultrices at a eros. Vivamus vulputate diam vitae eros tincidunt, eget sollicitudin odio imperdiet. In nec lacus massa. Sed luctus metus accumsan purus feugiat dictum. Aenean commodo augue eu felis maximus, sodales placerat lectus aliquam.</p>'''
            
            post.save()

        for i in range(1, 100):
            project = PortfolioProject()
            project.title = f'Project {i}'
            project.slug = f'project-{i}'
            project.image = 'coding_cropped.jpg'
            project.excerpt = '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla eu dui eget orci maximus placerat eu vitae leo. Sed nulla felis, convallis ut nibh at, mollis cursus erat. Cras quis enim gravida, feugiat eros vel, tempor quam.&nbsp;</p>'
            project.content = '''<p><strong>Lorem ipsum dolor sit amet</strong>, consectetur adipiscing elit. Nulla eu dui eget orci maximus placerat eu vitae leo. Sed nulla felis, convallis ut nibh at, mollis cursus erat. Cras quis enim gravida, feugiat eros vel, tempor quam. Morbi at ex egestas, sollicitudin mi ut, feugiat urna. Quisque arcu nisl, tempus vitae lobortis vel, varius eu lacus. Morbi rhoncus risus mollis est lobortis, id accumsan nulla blandit. Pellentesque neque orci, pulvinar at vehicula a, scelerisque nec orci. Proin ut ipsum in orci lacinia consequat ac et turpis. Nullam sodales fermentum pretium. In maximus nunc lacus, faucibus rhoncus turpis lobortis a. Sed sed mollis lectus. Nullam at nisi finibus, finibus nisi in, eleifend leo. Nunc sagittis ex placerat est ornare dictum vel non odio. Integer eget nibh a felis ullamcorper facilisis eget sit amet neque. Nulla viverra nisi at ex venenatis, ut euismod augue facilisis. Pellentesque elit dui, luctus et pretium at, elementum nec sapien.</p>

<p><img alt="" src="/files/django.png" style="height:137px; width:300px" /></p>

<p>Nulla ac nisi fermentum, posuere magna tincidunt, sollicitudin tellus. Quisque faucibus sagittis felis, vitae congue leo euismod eget. Vestibulum semper egestas sollicitudin. Vestibulum et neque ut diam efficitur mattis a non lectus. Duis vitae nunc molestie sapien semper iaculis. Aenean rutrum sagittis ligula, a dignissim enim pharetra id. In ac ligula dui.</p>

<p>In sem metus, gravida eget orci eget, lacinia pulvinar dui. Donec vitae arcu gravida, pulvinar sapien non, convallis justo. Mauris vitae facilisis dui. Praesent auctor sed orci ac aliquam. Sed interdum massa sit amet orci tincidunt, non lobortis magna luctus. Suspendisse pellentesque accumsan felis sit amet sollicitudin. Sed eu lobortis nisi. Nulla non risus in quam ornare finibus. Morbi ante magna, lobortis sed odio non, gravida rutrum felis. Aenean feugiat bibendum porttitor. Integer vehicula convallis ultrices. Proin sit amet dui arcu. Sed eleifend dolor quis finibus imperdiet. Mauris maximus, sem a sollicitudin vulputate, quam odio condimentum magna, at vulputate ante tellus vel quam. Pellentesque a tortor vel risus condimentum gravida id vel neque.</p>

<p>Suspendisse potenti. Donec vel justo leo. Sed venenatis, libero sit amet iaculis dapibus, quam magna faucibus leo, sit amet sodales enim ipsum vel velit. Ut rutrum tincidunt nisi sed blandit. Nullam imperdiet nisi mauris, sit amet interdum ex finibus et. Nullam scelerisque venenatis enim a interdum. Etiam pellentesque rutrum ullamcorper. Vestibulum sed neque nec sem aliquam consequat. Ut luctus molestie volutpat. Cras imperdiet erat eget arcu malesuada, non pellentesque est sollicitudin. Aliquam enim erat, varius in gravida non, fringilla eu ex. Etiam facilisis, ligula non rutrum egestas, libero lectus cursus turpis, ut ullamcorper tellus purus eu sem. Proin placerat sem non justo placerat convallis. Donec eleifend quam lacus, at dictum lorem bibendum id. In ut ante urna.</p>

<p>Etiam ac sapien et quam pretium auctor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eget malesuada mi. Nam convallis est eget aliquam lobortis. Mauris tristique congue mattis. Aliquam at eleifend neque, aliquam laoreet sapien. Quisque velit mauris, volutpat at odio ac, varius faucibus dolor. In eget odio eget leo pulvinar consequat a in leo. Ut sapien metus, pellentesque laoreet lacinia in, porttitor sed turpis. Fusce bibendum lacinia interdum. Sed a nunc in risus condimentum ultrices at a eros. Vivamus vulputate diam vitae eros tincidunt, eget sollicitudin odio imperdiet. In nec lacus massa. Sed luctus metus accumsan purus feugiat dictum. Aenean commodo augue eu felis maximus, sodales placerat lectus aliquam.</p>'''

            project.save()

        self.stdout.write(self.style.SUCCESS('Dummy data created!'))
