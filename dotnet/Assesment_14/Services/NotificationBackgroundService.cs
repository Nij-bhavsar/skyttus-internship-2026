using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace Assesment_14.Services
{
    public class NotificationBackgroundService : BackgroundService
    {
        private readonly ILogger<NotificationBackgroundService> _logger;
        private readonly EmailService _emailService;
        private readonly SmsService _smsService;

        public NotificationBackgroundService(
            ILogger<NotificationBackgroundService> logger,
            EmailService emailService,
            SmsService smsService)
        {
            _logger = logger;
            _emailService = emailService;
            _smsService = smsService;
        }

        protected override async Task ExecuteAsync(CancellationToken stoppingToken)
        {
            _logger.LogInformation("Background Notification Service started.");

            while (!stoppingToken.IsCancellationRequested)
            {
                try
                {
                    _logger.LogInformation("Background job running at {Time}", DateTime.Now);

                    // Email
                    await _emailService.SendEmailAsync(
                        "receiver-email@gmail.com",
                        "Scheduled Notification",
                        "This email is sent every 1 minute from background service."
                    );

                    // SMS (Mock)
                    await _smsService.SendSmsAsync(
                        "+91XXXXXXXXXX",
                        "Scheduled SMS notification from background service."
                    );

                    _logger.LogInformation("Notifications sent successfully.");
                }
                catch (Exception ex)
                {
                    _logger.LogError(ex, "Error occurred in background job.");
                }

                await Task.Delay(TimeSpan.FromMinutes(1), stoppingToken);
            }
        }
    }
}