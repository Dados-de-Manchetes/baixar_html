output "aws_instance_padrao_id" {
  value       = aws_instance.baixar_html.id
  description = "Id da instancia criada"
}

output "aws_iam_role_instancia" {
  value = aws_iam_role.baixar_html.id
  description = "Id da role criada"
}