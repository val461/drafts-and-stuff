(ns clojure-noob.core
  (:gen-class))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "I'm a happy teapot!"))
(println "RE2AD")

(defn add100
  [n]
  (+ n 100))

(defn dec-maker
  [dec-by]
  (fn [n] (- n dec-by)))
