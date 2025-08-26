// Example program:
// Using SDL3 to create an application window

#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include <SDL3_image/SDL_image.h>
#include <SDL3/SDL_render.h>
#include <SDL3/SDL_iostream.h>
#include <iostream>
#include <StartScreen.hpp>
#include <StringConstants.hpp>
#include <string>
#include <stdio.h>
#include <unistd.h>
#include<App.hpp>


#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 480

/// @brief 
/// @param argc 
/// @param argv 
/// @return 
int main(int argc, char* argv[]) {

    App * appInstance = &App::getInstance();
    if (!SDL_Init(SDL_INIT_VIDEO)) {
        SDL_Log("Couldn't initialize SDL: %s", SDL_GetError());
        return SDL_APP_FAILURE;
    }

    bool done = false;




    if(!SDL_SetAppMetadata(APP_NAME.c_str(), APP_VERSION.c_str(), APP_IDENTIFIER.c_str())){
        return 0;
    };

    SDL_Window * app_window = appInstance->getWindow();
    SDL_Renderer * app_renderer = appInstance->getRenderer();
    // Create window and renderer (appTitle, w, h , windowType, x , x)
    SDL_CreateWindowAndRenderer(APP_NAME.c_str(), 2000, 500, 0, &app_window, &app_renderer);

    // Set the working directory
    const char *new_wd = WORKING_DIR.c_str(); // Replace with your project root
    if (chdir(new_wd) != 0) {
        SDL_Log("chdir failed: %s", strerror(errno));
    }

    // Open the PNG file as an SDL_IOStream
    SDL_IOStream *io = SDL_IOFromFile(GAME_TITLE_PNG.c_str(), "rb");
    if (!io) {
        SDL_Log("SDL_IOFromFile failed: %s", SDL_GetError());
        SDL_DestroyRenderer(app_renderer);
        SDL_DestroyWindow(app_window);
        SDL_Quit();
        return 1;
    }

    
    // Load the PNG image using IMG_LoadPNG_IO
    SDL_Surface *surface = IMG_LoadPNG_IO(io);
    if (!surface) {
        SDL_CloseIO(io);
        SDL_DestroyRenderer(app_renderer);
        SDL_DestroyWindow(app_window);
        SDL_Quit();
        return 1;
    }

    int texture_width = surface->w;
    int texture_height = surface->h;

    SDL_CloseIO(io); // Close the IO stream


    if (!app_window || !app_renderer) 
    {
        SDL_LogError(SDL_LOG_CATEGORY_ERROR, "Could not create window or renderer: %s\n", SDL_GetError());
        // Handle error
        return -1;
    }

    // Create texture from surface
    SDL_Texture *texture = SDL_CreateTextureFromSurface(app_renderer, surface);
    if (!texture) {
        SDL_Log("SDL_CreateTextureFromSurface failed: %s", SDL_GetError());
        SDL_DestroySurface(surface);
        SDL_DestroyRenderer(app_renderer);
        SDL_DestroyWindow(app_window);
        SDL_Quit();
        return 1;
    }
    SDL_DestroySurface(surface); // Free the surface

     SDL_FRect dst_rect;
    const Uint64 now = SDL_GetTicks();

    /* we'll have the texture grow and shrink over a few seconds. */
    const float direction = ((now % 2000) >= 1000) ? 1.0f : -1.0f;
    const float scale = ((float) (((int) (now % 1000)) - 500) / 500.0f) * direction;

    /* as you can see from this, rendering draws over whatever was drawn before it. */
    SDL_SetRenderDrawColor(app_renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);  /* black, full alpha */
    SDL_RenderClear(app_renderer);  /* start with a blank canvas. */

    /* center this one and make it grow and shrink. */
    dst_rect.w = (float) texture_width;
    dst_rect.h = (float) texture_height;
    dst_rect.x = (WINDOW_WIDTH - dst_rect.w) / 2.0f;
    dst_rect.y = (WINDOW_HEIGHT - dst_rect.h) / 2.0f;
    SDL_RenderTexture(app_renderer, texture, NULL, &dst_rect);

    SDL_RenderPresent(app_renderer);  /* put it all on the screen! */

    while (!done) {
        SDL_Event event;
        //SDL_SetWindowFullscreen(app_window, true);
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_EVENT_QUIT) {
                done = true;
            }
        }

        // Do game logic, present a frame, etc.
    }

    // Close and destroy the window
    SDL_DestroyWindow(app_window);

    // Clean up
    SDL_Quit();
    return 0;
}