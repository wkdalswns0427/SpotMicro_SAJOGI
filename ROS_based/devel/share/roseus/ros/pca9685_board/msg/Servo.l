;; Auto-generated. Do not edit!


(when (boundp 'pca9685_board::Servo)
  (if (not (find-package "PCA9685_BOARD"))
    (make-package "PCA9685_BOARD"))
  (shadow 'Servo (find-package "PCA9685_BOARD")))
(unless (find-package "PCA9685_BOARD::SERVO")
  (make-package "PCA9685_BOARD::SERVO"))

(in-package "ROS")
;;//! \htmlinclude Servo.msg.html


(defclass pca9685_board::Servo
  :super ros::object
  :slots (_name _value ))

(defmethod pca9685_board::Servo
  (:init
   (&key
    ((:name __name) "")
    ((:value __value) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _value (float __value))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; float32 _value
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float32 _value
       (sys::poke _value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _value
     (setq _value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pca9685_board::Servo :md5sum-) "db3486341a840969e8845548decf6f11")
(setf (get pca9685_board::Servo :datatype-) "pca9685_board/Servo")
(setf (get pca9685_board::Servo :definition-)
      "# the Servo message is commonly used message in this package to
# assign a value to a specific servo. the purpose of the value is
# dependent on the topic or service being called

string name
float32 value

")



(provide :pca9685_board/Servo "db3486341a840969e8845548decf6f11")


