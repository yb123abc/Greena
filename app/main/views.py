#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
#from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
	form = []
	products = ['紫甘菜', '西红柿' ,'三文鱼','鸡脯肉','甘蓝菜','敬请期待'] 
	#form = NameForm()
	#if form.validate_on_submit():

	#	return redirect(url_for('.index'))
	return render_template('index.html',
		form=form, name=session.get('name'),
		known=session.get('known', False),
		products=products, 
		current_time=datetime.utcnow())
