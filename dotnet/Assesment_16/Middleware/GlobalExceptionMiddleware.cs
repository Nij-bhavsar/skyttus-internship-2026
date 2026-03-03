using System.Net;
using System.Text.Json;

namespace Assesment_16.Middleware
{
    public class GlobalExceptionMiddleware
    {
        private readonly RequestDelegate _next;
        private readonly IWebHostEnvironment _env;

        public GlobalExceptionMiddleware(RequestDelegate next, IWebHostEnvironment env)
        {
            _next = next;
            _env = env;
        }

        public async Task InvokeAsync(HttpContext context)
        {
            try
            {
                await _next(context);
            }
            catch (Exception ex)
            {
                context.Response.StatusCode = (int)HttpStatusCode.InternalServerError;
                context.Response.ContentType = "application/json";

                var response = new Dictionary<string, object?>
                {
                    { "message", _env.IsDevelopment() ? ex.Message : "An unexpected error occurred." }
                };

                if (_env.IsDevelopment())
                {
                    response.Add("stackTrace", ex.StackTrace);
                }

                await context.Response.WriteAsync(JsonSerializer.Serialize(response));
            }
        }
    }
}