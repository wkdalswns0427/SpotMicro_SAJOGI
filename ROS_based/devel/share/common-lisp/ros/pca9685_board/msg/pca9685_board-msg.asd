
(cl:in-package :asdf)

(defsystem "pca9685_board-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Servo" :depends-on ("_package_Servo"))
    (:file "_package_Servo" :depends-on ("_package"))
  ))