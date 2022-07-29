# Como tornar uma subnet publica? https://medium.com/@aliatakan/terraform-create-a-vpc-subnets-and-more-6ef43f0bf4c1
resource "aws_instance" "baixar_html" {

  ami           = "ami-0f9fc25dd2506cf6d" # Amazon linux 2
  instance_type = "t3a.small"
  iam_instance_profile = "${aws_iam_instance_profile.baixar_html.id}"

  vpc_security_group_ids = [aws_security_group.baixar_html.id]
  subnet_id   = "subnet-06b0fcfe6d317bb93"
  private_ip = "172.16.10.11"
  associate_public_ip_address = true

  user_data = "${file("./files/app_run.sh")}"

  root_block_device {
      volume_size = "8"
      volume_type = "gp3"
  }

  tags = {
    projeto = var.projeto_tag
    Name = "${var.app_baixar_html_nome}"
  }
}

resource "aws_security_group" "baixar_html" {
  vpc_id = "vpc-0a43627375b3b3495"
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks =  ["0.0.0.0/0"]
  } 

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "all"
    cidr_blocks =  ["0.0.0.0/0"]
  }
}

resource "aws_iam_instance_profile" "baixar_html" {
    name = "${var.projeto_tag}-${var.app_baixar_html_nome}-iam-instance"
    role = aws_iam_role.baixar_html.id
}

resource "aws_iam_role" "baixar_html" {
    name = "${var.projeto_tag}-${var.app_baixar_html_nome}-iam-role"
    assume_role_policy = "${file("./files/role/instance.json")}"
}

resource "aws_iam_role_policy" "s3_code_base" {
  name = "${var.projeto_tag}-${var.app_baixar_html_nome}-iam-role-policy-s3-code-base"
  role = "${aws_iam_role.baixar_html.id}"
  policy = "${file("./files/policy/s3_code_base.json")}"
}

resource "aws_iam_role_policy" "s3_manchetes_dados" {
  name = "${var.projeto_tag}-${var.app_baixar_html_nome}-iam-role-policy-s3-manchetes-dados"
  role = "${aws_iam_role.baixar_html.id}"
  policy = "${file("./files/policy/s3_manchetes-dados.json")}"
}

resource "aws_iam_role_policy" "s3_manchetes-url-data" {
  name = "${var.projeto_tag}-${var.app_baixar_html_nome}-iam-role-policy-s3-dados-gerais"
  role = "${aws_iam_role.baixar_html.id}"
  policy = "${file("./files/policy/s3_manchetes-url-data.json")}"
}