#ifndef GDEXAMPLE_H
#define GDEXAMPLE_H

#include <godot_cpp/classes/sprite2d.hpp>


namespace godot {

class GDExample : public Sprite2D {
    GDCLASS(GDExample, Sprite2D)

private:
    double time_passed;
    double amplitude;
    double speed;

protected:
    static void _bind_methods();

public:
    GDExample();
    ~GDExample();

    void _process(double delta) override;
    
    void set_amplitude(const double p_amplitude);
	double get_amplitude() const;
    void set_speed(const double p_speed);
	double get_speed() const;

};

}




#endif // GDEXAMPLE_H


