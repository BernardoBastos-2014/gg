extends CharacterBody3D

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		rotation_degrees.y -= event.relative.x * 0.5
		%Camera3D.rotation_degrees.x -= event.relative.y *0.2
		%Camera3D.rotation_degrees.x = clamp(
			%Camera3D.rotation_degrees.x,-60.0,60.0
		)
	elif event.is_action_pressed("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
	elif event.is_action_pressed("ui_accept"):
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _ready() -> void:
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
func _physics_process(delta: float) -> void:
	const SPEED = 5.5
	var input_direction_2D = Input.get_vector(
		"move L","move R" , "move F", "move B"
	)
	var input_direction_3D = Vector3(
		input_direction_2D.x, 0, input_direction_2D.y
	)
	var direction = transform.basis * input_direction_3D
	velocity.x = direction.x * SPEED
	velocity.z = direction.z * SPEED
	velocity.y -= 20.0 * delta
	
	if Input.is_action_just_pressed("Jump") and is_on_floor():
		velocity.y = 5.0
	elif Input.is_action_just_released("Jump") and velocity.y > 0.0:
		velocity.y *= 0.5
	move_and_slide()
