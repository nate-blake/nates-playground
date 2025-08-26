#ifndef _APP_HPP
#define _APP_HPP
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

class App
{


    private:
        SDL_Window *m_window; 
        SDL_Renderer* m_renderer;
    App()
    {
        m_window = NULL;
        m_renderer = NULL; 
    };

    App(const App&) = delete;
    App& operator=(const App&) = delete;

    public:
        static App& getInstance()
        {
            static App instance;
            return instance;
        }

        SDL_Window* getWindow(){
            return m_window;
        }
        SDL_Renderer* getRenderer(){
            return m_renderer;
        }

};
#endif