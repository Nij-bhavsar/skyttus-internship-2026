using Microsoft.Extensions.Logging;

namespace Assesment_14.Services
{
    public class SmsService
    {
        private readonly ILogger<SmsService> _logger;

        public SmsService(ILogger<SmsService> logger)
        {
            _logger = logger;
        }

        public Task SendSmsAsync(string number, string message)
        {
            _logger.LogInformation(
                "Mock SMS sent to {Number}: {Message}",
                number,
                message
            );

            return Task.CompletedTask;
        }
    }
}