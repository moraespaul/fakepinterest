# Criar os formularios do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário Inexistente, crie uma conta para continuar.')

    def validate_senha(self, senha):
        usuario = Usuario.query.filter_by(senha=senha.data).first()
        if not usuario:
            raise ValidationError('Senha invalida.')


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6,20)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Cadastrar')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado, faça login para continuar')




class FormFoto(FlaskForm):
    foto = FileField('Foto', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Enviar')