variable "aws_region" {
  type        = string
  description = "Regiao de downlaod"
  default     = "us-east-1"
}

variable "app_baixar_html_nome" {
  type = string
  description = "Nome da aplicação padrão"
}

variable "projeto_tag" {
  type        = string
  description = "O nome do projeto para utilizar nos tags"
}