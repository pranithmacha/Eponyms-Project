from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from tumbleblog.models import Eponyms

posts = Blueprint('posts',__name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        eponyms = Eponyms.objects.all()
        return render_template('posts/list.html',eponyms=eponyms)

class DetailView(MethodView):
    def get(self,subject_name):
        post = Eponyms.objects.get_or_404(subject_name=subject_name)
        return render_template('posts/detail.html', post=post)

class WritePageView(MethodView):
    def get(self):
        return render_template('write.html')

class HomePageView(MethodView):
    def get(self):
        return render_template('homepage.html')
class HomeRequestView(MethodView):
    def post(self):
      eponym_name = request.form['eponym_name']
      subject_name = request.form['subject_name']
      eponym_description = request.form['eponym_description']
      references = request.form['references']
      post = Eponyms(subject_name=subject_name, eponym_name=eponym_name, eponym_description=eponym_description, references=references)
      post.save()
      return render_template('result.html',subject_name=subject_name,eponym_name=eponym_name)

# Register the urls
posts.add_url_rule('/eponym_post',view_func = HomeRequestView.as_view('result'))
posts.add_url_rule('/', view_func = HomePageView.as_view('home'))
posts.add_url_rule('/<subject_name>/', view_func = DetailView.as_view('detail'))
posts.add_url_rule('/write', view_func = WritePageView.as_view('write'))
posts.add_url_rule('/homepage', view_func = HomePageView.as_view('homepage'))

   



